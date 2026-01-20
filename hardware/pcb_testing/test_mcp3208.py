#!/usr/bin/env python3
"""
Test script for MCP3208 ADC validation
Script de test pour validation du MCP3208 ADC
"""

import spidev
import time
import sys

class MCP3208Tester:
    def __init__(self):
        self.spi = None
        
    def initialize_spi(self):
        """Initialize SPI connection / Initialiser la connexion SPI"""
        try:
            self.spi = spidev.SpiDev()
            self.spi.open(0, 0)  # Bus 0, Device 0
            self.spi.max_speed_hz = 1000000  # 1MHz
            self.spi.mode = 0
            print("✓ SPI initialized / SPI initialisé")
            return True
        except Exception as e:
            print(f"✗ SPI initialization error / Erreur d'initialisation SPI: {e}")
            return False
    
    def read_channel(self, channel):
        """Read MCP3208 channel / Lire un canal du MCP3208"""
        if self.spi is None:
            print("Error: SPI not initialized / Erreur: SPI non initialisé")
            return None
        
        if not (0 <= channel <= 7):
            print(f"Error: Invalid channel {channel} / Erreur: Canal invalide {channel}")
            return None
        
        try:
            # Build read command
            # Single-ended read: start bit (1), SGL/DIFF (1), Channel (3 bits)
            cmd = 0x06 | ((channel & 0x07) >> 2)
            cmd2 = (channel & 0x03) << 6
            
            # Send command and read response
            response = self.spi.xfer2([cmd, cmd2, 0x00])
            
            # Extract 12-bit value
            value = ((response[0] & 0x01) << 11) | (response[1] << 3) | (response[2] >> 5)
            
            return value
        except Exception as e:
            print(f"✗ Read error / Erreur de lecture: {e}")
            return None
    
    @staticmethod
    def adc_to_voltage(value, vref=3.3):
        """Convert ADC value to voltage / Convertir valeur ADC en tension"""
        if value is None:
            return None
        return (value / 4095.0) * vref
    
    def test_communication(self):
        """Test basic SPI communication / Tester la communication SPI de base"""
        print("\nCommunication test / Test de communication...")
        
        try:
            value = self.read_channel(0)
            if value is not None:
                voltage = self.adc_to_voltage(value)
                print(f"✓ Read successful: {value} (0x{value:03X}), {voltage:.4f}V")
                return True
            else:
                print("✗ Read failed / Lecture échouée")
                return False
        except Exception as e:
            print(f"✗ Communication error / Erreur de communication: {e}")
            return False
    
    def test_reference(self):
        """Test voltage reference / Tester la référence de tension"""
        print("\nReference test / Test de référence...")
        print("This test requires manual connection of channels to GND and VCC")
        print("Ce test nécessite la connexion manuelle des canaux à GND et VCC")
        
        all_passed = True
        
        for channel in range(8):
            print(f"\n--- Channel {channel} ---")
            
            # Test GND
            input(f"Connect channel {channel} to GND, then press Enter...")
            input(f"Connecter canal {channel} à GND, puis appuyer sur Enter...")
            
            values = [self.read_channel(channel) for _ in range(10)]
            avg_value = sum(values) / len(values)
            voltage = self.adc_to_voltage(avg_value)
            
            print(f"GND reading: {avg_value:.1f} ({voltage:.4f}V)")
            
            if avg_value < 50:
                print(f"✓ GND test PASSED for channel {channel}")
            else:
                print(f"✗ GND test FAILED for channel {channel} - value too high")
                all_passed = False
            
            # Test VCC
            input(f"Connect channel {channel} to 3.3V, then press Enter...")
            input(f"Connecter canal {channel} à 3.3V, puis appuyer sur Enter...")
            
            values = [self.read_channel(channel) for _ in range(10)]
            avg_value = sum(values) / len(values)
            voltage = self.adc_to_voltage(avg_value)
            
            print(f"VCC reading: {avg_value:.1f} ({voltage:.4f}V)")
            
            if avg_value > 4000:
                print(f"✓ VCC test PASSED for channel {channel}")
            else:
                print(f"✗ VCC test FAILED for channel {channel} - value too low")
                all_passed = False
        
        return all_passed
    
    def test_linearity(self, channel=0):
        """Test ADC linearity / Tester la linéarité de l'ADC"""
        print(f"\nLinearity test on channel {channel}")
        print(f"Test de linéarité sur le canal {channel}")
        print("This test requires applying known voltages")
        print("Ce test nécessite l'application de tensions connues")
        
        test_voltages = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
        all_passed = True
        
        for v in test_voltages:
            input(f"\nApply {v}V to channel {channel}, then press Enter...")
            input(f"Appliquer {v}V au canal {channel}, puis appuyer sur Enter...")
            
            # Read multiple times and average
            values = [self.read_channel(channel) for _ in range(20)]
            avg_value = sum(values) / len(values)
            measured_v = self.adc_to_voltage(avg_value)
            
            error = abs(measured_v - v)
            print(f"Expected: {v}V, Measured: {measured_v:.4f}V, Error: {error:.4f}V")
            
            # Tolerance ±50mV
            if error < 0.05:
                print(f"✓ Linearity test PASSED at {v}V")
            else:
                print(f"✗ Linearity test FAILED at {v}V - error too large")
                all_passed = False
        
        return all_passed
    
    def test_noise(self, channel=0, num_samples=100):
        """Test ADC noise / Tester le bruit de l'ADC"""
        print(f"\nNoise test on channel {channel}")
        print(f"Test de bruit sur le canal {channel}")
        print("Connect channel to stable voltage (e.g., 1.65V using voltage divider)")
        print("Connecter le canal à une tension stable (ex: 1.65V avec diviseur)")
        input("Press Enter when ready / Appuyer sur Enter quand prêt...")
        
        # Collect samples
        samples = []
        for _ in range(num_samples):
            value = self.read_channel(channel)
            if value is not None:
                samples.append(value)
            time.sleep(0.01)
        
        # Analyze
        mean_value = sum(samples) / len(samples)
        variance = sum((x - mean_value)**2 for x in samples) / len(samples)
        std_dev = variance ** 0.5
        
        min_val = min(samples)
        max_val = max(samples)
        range_val = max_val - min_val
        
        print(f"Mean: {mean_value:.2f} ({self.adc_to_voltage(mean_value):.4f}V)")
        print(f"Std Dev: {std_dev:.2f} ({self.adc_to_voltage(std_dev):.4f}V)")
        print(f"Range: {range_val} ({self.adc_to_voltage(range_val):.4f}V)")
        print(f"Min: {min_val}, Max: {max_val}")
        
        # Validation - std dev should be low
        if std_dev < 5:
            print("✓ Noise test PASSED - low noise")
            return True
        else:
            print("✗ Noise test FAILED - noise too high")
            return False
    
    def test_all_channels(self):
        """Quick test of all channels / Test rapide de tous les canaux"""
        print("\nAll channels test / Test de tous les canaux...")
        print("Reading all 8 channels / Lecture des 8 canaux")
        
        for channel in range(8):
            value = self.read_channel(channel)
            voltage = self.adc_to_voltage(value)
            print(f"Channel {channel}: {value:4d} (0x{value:03X}), {voltage:.4f}V")
        
        return True
    
    def run_all_tests(self):
        """Run all MCP3208 tests / Exécuter tous les tests MCP3208"""
        print("="*50)
        print("MCP3208 VALIDATION TEST / TEST DE VALIDATION MCP3208")
        print("="*50)
        
        results = {}
        
        # Initialization
        results['initialization'] = self.initialize_spi()
        if not results['initialization']:
            return results
        
        # Communication
        results['communication'] = self.test_communication()
        if not results['communication']:
            return results
        
        # All channels quick test
        results['all_channels'] = self.test_all_channels()
        
        # Ask user which detailed tests to run
        print("\nDetailed tests require manual voltage application")
        print("Les tests détaillés nécessitent l'application manuelle de tensions")
        
        run_reference = input("\nRun reference test (GND/VCC)? (y/n): ").lower() == 'y'
        if run_reference:
            results['reference'] = self.test_reference()
        
        run_linearity = input("\nRun linearity test? (y/n): ").lower() == 'y'
        if run_linearity:
            results['linearity'] = self.test_linearity()
        
        run_noise = input("\nRun noise test? (y/n): ").lower() == 'y'
        if run_noise:
            results['noise'] = self.test_noise()
        
        return results
    
    def cleanup(self):
        """Cleanup SPI connection / Nettoyer la connexion SPI"""
        if self.spi:
            self.spi.close()
            print("SPI closed / SPI fermé")


def main():
    tester = MCP3208Tester()
    
    try:
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
            return_code = 0
        else:
            print("✗ SOME TESTS FAILED / CERTAINS TESTS ÉCHOUÉS")
            return_code = 1
        
        tester.cleanup()
        return return_code
        
    except KeyboardInterrupt:
        print("\n\nTest interrupted / Test interrompu")
        tester.cleanup()
        return 1


if __name__ == "__main__":
    sys.exit(main())
