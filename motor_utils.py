# I2C address of the LSM6DSOX (0x6A if SA0 pin is low, otherwise 0x6B)
LSM6DSOX_ADDR = 0x6A

# I2C bus (1 for Raspberry Pi)
i2cbus = 1

# Number of bytes to read for gyro and accel
NUM_BYTES = 6   # renommé (bytes est un mot-clé Python réservé)

# Frequency settings for accelerometer
FQ_POWER_DOWN = 0x00
FQ12_5HZ      = 0x10
FQ26HZ        = 0x20
FQ52HZ        = 0x30
FQ104HZ       = 0x40
FQ208HZ       = 0x50
FQ416HZ       = 0x60
FQ833HZ       = 0x70
FQ1660HZ      = 0x80
FQ3330HZ      = 0x90
FQ6660HZ      = 0xA0

# Accelerometer full-scale selection
FS_2G  = 0x00
FS_16G = 0x04
FS_4G  = 0x08
FS_8G  = 0x0C

# Gyroscope frequencies
FQ_G_POWER_DOWN = 0x00
FQ_G_12_5HZ     = 0x10
FQ_G_26HZ       = 0x20
FQ_G_52HZ       = 0x30
FQ_G_104HZ      = 0x40
FQ_G_208HZ      = 0x50
FQ_G_416HZ      = 0x60
FQ_G_833HZ      = 0x70
FQ_G_1660HZ     = 0x80
FQ_G_3330HZ     = 0x90
FQ_G_6660HZ     = 0xA0

# Gyroscope full scale
FS_G_125DPS  = 0x02
FS_G_245DPS  = 0x00
FS_G_500DPS  = 0x04
FS_G_1000DPS = 0x08
FS_G_2000DPS = 0x0C

# CTRL3_C register bits
CTRL3_C_BOOT      = 0x80
CTRL3_C_BDU       = 0x40
CTRL3_C_H_LACTIVE = 0x20
CTRL3_C_PP_OD     = 0x10
CTRL3_C_SIM       = 0x08
CTRL3_C_IF_INC    = 0x04
CTRL3_C_SW_RESET  = 0x01

# Time delay for each data read (in seconds)
time_delay = 1

# Scale factors — accelerometer (LSB/g)
SF_2G  = 0.000061
SF_4G  = 0.000122
SF_8G  = 0.000244
SF_16G = 0.000488

# Scale factors — gyroscope (LSB/dps)
SF_200DPS  = 0.00875
SF_500DPS  = 0.0175
SF_1000DPS = 0.035
SF_2000DPS = 0.07
