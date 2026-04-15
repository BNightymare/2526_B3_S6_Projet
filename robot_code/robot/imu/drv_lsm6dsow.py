import smbus2
import time
from .setting import *


CTRL1_XL  = 0x10
CTRL2_G   = 0x11
CTRL3_C   = 0x12
OUTX_L_G  = 0x22
OUTX_L_XL = 0x28


class drv_lsm6dsow:
    def __init__(self, bus=i2cbus, adresse=LSM6DSOX_ADDR):
        self.bus     = smbus2.SMBus(bus)
        self.adresse = adresse
        self.init_lsm6dsox()

    def init_lsm6dsox(self):
        self.bus.write_byte_data(self.adresse, CTRL1_XL, FQ104HZ | FS_2G)
        self.bus.write_byte_data(self.adresse, CTRL2_G,  FQ_G_104HZ | FS_G_245DPS)
        self.bus.write_byte_data(self.adresse, CTRL3_C,  CTRL3_C_BDU | CTRL3_C_IF_INC)
        time.sleep(0.1)

    def read_accel(self):
        data = self.bus.read_i2c_block_data(self.adresse, OUTX_L_XL, NUM_BYTES)
        x = self._twos_complement(data[1] << 8 | data[0], 16)
        y = self._twos_complement(data[3] << 8 | data[2], 16)
        z = self._twos_complement(data[5] << 8 | data[4], 16)
        return x, y, z

    def read_gyro(self):
        data = self.bus.read_i2c_block_data(self.adresse, OUTX_L_G, NUM_BYTES)
        x = self._twos_complement(data[1] << 8 | data[0], 16)
        y = self._twos_complement(data[3] << 8 | data[2], 16)
        z = self._twos_complement(data[5] << 8 | data[4], 16)
        return x, y, z

    def _twos_complement(self, val, bits):
        if val & (1 << (bits - 1)):
            val -= 1 << bits
        return val
