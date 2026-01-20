#!/usr/bin/env python3
"""
Test script for IMU validation
Script de test pour validation de l'IMU
"""

import smbus
import time
import sys

# Configuration
I2C_BUS = 1
IMU_ADDR_DEFAULT = 0x68  # MPU6050 default address
IMU_ADDR_ALT = 0x69      # Alternative address

class IMUTester:
    def __init__(self, bus_number=I2C_BUS):
        self.bus = smbus.SMBus(bus_number)
        self.imu_addr = None
        
    def detect_imu(self):
        """Detect IMU on I2C bus / Détecter l'IMU sur le bus I2C"""
        print("Detecting IMU... / Détection de l'IMU...")
        
        for addr in [IMU_ADDR_DEFAULT, IMU_ADDR_ALT]:
            try:
                who_am_i = self.bus.read_byte_data(addr, 0x75)
                print(f"✓ IMU found at address 0x{addr:02X}, WHO_AM_I=0x{who_am_i:02X}")
                self.imu_addr = addr
                return True
            except:
                continue
        
        print("✗ IMU not found / IMU non trouvée")
        return False
    
    def initialize_imu(self):
        """Initialize IMU / Initialiser l'IMU"""
        if not self.imu_addr:
            print("Error: IMU not detected / Erreur: IMU non détectée")
            return False
        
        try:
            # Reset
            self.bus.write_byte_data(self.imu_addr, 0x6B, 0x80)
            time.sleep(0.1)
            
            # Wake up
            self.bus.write_byte_data(self.imu_addr, 0x6B, 0x00)
            time.sleep(0.1)
            
            # Configure gyro (±250°/s)
            self.bus.write_byte_data(self.imu_addr, 0x1B, 0x00)
            
            # Configure accel (±2g)
            self.bus.write_byte_data(self.imu_addr, 0x1C, 0x00)
            
            # Enable low-pass filter
            self.bus.write_byte_data(self.imu_addr, 0x1A, 0x03)
            
            print("✓ IMU initialized / IMU initialisée")
            return True
        except Exception as e:
            print(f"✗ Initialization error / Erreur d'initialisation: {e}")
            return False
    
    def read_data(self):
        """Read IMU data / Lire les données de l'IMU"""
        try:
            data = self.bus.read_i2c_block_data(self.imu_addr, 0x3B, 14)
            
            # Parse accelerometer
            accel_x = self._to_signed(((data[0] << 8) | data[1]))
            accel_y = self._to_signed(((data[2] << 8) | data[3]))
            accel_z = self._to_signed(((data[4] << 8) | data[5]))
            
            # Parse temperature
            temp_raw = self._to_signed(((data[6] << 8) | data[7]))
            temp = (temp_raw / 340.0) + 36.53
            
            # Parse gyroscope
            gyro_x = self._to_signed(((data[8] << 8) | data[9]))
            gyro_y = self._to_signed(((data[10] << 8) | data[11]))
            gyro_z = self._to_signed(((data[12] << 8) | data[13]))
            
            return {
                'accel': (accel_x, accel_y, accel_z),
                'gyro': (gyro_x, gyro_y, gyro_z),
                'temp': temp
            }
        except Exception as e:
            print(f"✗ Read error / Erreur de lecture: {e}")
            return None
    
    @staticmethod
    def _to_signed(value):
        """Convert to signed 16-bit / Convertir en 16-bit signé"""
        if value > 32767:
            value -= 65536
        return value
    
    def test_gravity(self, num_samples=10):
        """Test static gravity / Tester la gravité statique"""
        print("\nGravity test / Test de gravité...")
        print("Place PCB flat / Placer le PCB à plat")
        input("Press Enter when ready / Appuyer sur Enter quand prêt...")
        
        accel_x_sum = 0
        accel_y_sum = 0
        accel_z_sum = 0
        
        for i in range(num_samples):
            data = self.read_data()
            if data:
                accel_x_sum += data['accel'][0]
                accel_y_sum += data['accel'][1]
                accel_z_sum += data['accel'][2]
            time.sleep(0.1)
        
        avg_x = accel_x_sum / num_samples
        avg_y = accel_y_sum / num_samples
        avg_z = accel_z_sum / num_samples
        
        print(f"Average X: {avg_x:.0f} (expected ~0)")
        print(f"Average Y: {avg_y:.0f} (expected ~0)")
        print(f"Average Z: {avg_z:.0f} (expected ~16384 for ±2g)")
        
        # Validation
        x_ok = abs(avg_x) < 2000
        y_ok = abs(avg_y) < 2000
        z_ok = 14000 < abs(avg_z) < 18000
        
        if x_ok and y_ok and z_ok:
            print("✓ Gravity test PASSED")
            return True
        else:
            print("✗ Gravity test FAILED")
            return False
    
    def test_rotation(self, duration=5):
        """Test gyroscope rotation / Tester la rotation du gyroscope"""
        print("\nRotation test / Test de rotation...")
        print(f"Slowly rotate PCB for {duration} seconds")
        print(f"Faire pivoter lentement le PCB pendant {duration} secondes")
        input("Press Enter when ready / Appuyer sur Enter quand prêt...")
        
        max_gyro = 0
        start_time = time.time()
        
        while time.time() - start_time < duration:
            data = self.read_data()
            if data:
                gyro_magnitude = (data['gyro'][0]**2 + data['gyro'][1]**2 + data['gyro'][2]**2) ** 0.5
                max_gyro = max(max_gyro, gyro_magnitude)
                print(f"Gyro (x,y,z): {data['gyro']}, magnitude: {gyro_magnitude:.0f}")
            time.sleep(0.2)
        
        print(f"Max gyro magnitude: {max_gyro:.0f}")
        
        if max_gyro > 1000:
            print("✓ Rotation test PASSED")
            return True
        else:
            print("✗ Rotation test FAILED - no significant rotation detected")
            return False
    
    def test_temperature(self):
        """Test temperature sensor / Tester le capteur de température"""
        print("\nTemperature test / Test de température...")
        
        temps = []
        for i in range(10):
            data = self.read_data()
            if data:
                temps.append(data['temp'])
            time.sleep(0.1)
        
        avg_temp = sum(temps) / len(temps)
        print(f"Average temperature: {avg_temp:.2f}°C")
        
        if 15 < avg_temp < 40:
            print("✓ Temperature test PASSED")
            return True
        else:
            print("✗ Temperature test FAILED - temperature out of range")
            return False
    
    def run_all_tests(self):
        """Run all IMU tests / Exécuter tous les tests IMU"""
        print("="*50)
        print("IMU VALIDATION TEST / TEST DE VALIDATION IMU")
        print("="*50)
        
        results = {}
        
        # Detection
        results['detection'] = self.detect_imu()
        if not results['detection']:
            return results
        
        # Initialization
        results['initialization'] = self.initialize_imu()
        if not results['initialization']:
            return results
        
        # Data reading
        print("\nData reading test / Test de lecture...")
        for i in range(5):
            data = self.read_data()
            if data:
                print(f"Sample {i+1}:")
                print(f"  Accel: {data['accel']}")
                print(f"  Gyro:  {data['gyro']}")
                print(f"  Temp:  {data['temp']:.2f}°C")
                results['reading'] = True
            else:
                results['reading'] = False
                break
            time.sleep(0.2)
        
        if not results.get('reading'):
            return results
        
        # Specific tests
        results['gravity'] = self.test_gravity()
        results['rotation'] = self.test_rotation()
        results['temperature'] = self.test_temperature()
        
        return results


def main():
    tester = IMUTester()
    results = tester.run_all_tests()
    
    print("\n" + "="*50)
    print("TEST RESULTS / RÉSULTATS DES TESTS")
    print("="*50)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{test_name:20s}: {status}")
    
    all_passed = all(results.values())
    
    print("="*50)
    if all_passed:
        print("✓ ALL TESTS PASSED / TOUS LES TESTS RÉUSSIS")
        return 0
    else:
        print("✗ SOME TESTS FAILED / CERTAINS TESTS ÉCHOUÉS")
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nTest interrupted / Test interrompu")
        sys.exit(1)
