import time
import spidev

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=100000

while True:
	resp = spi.xfer([0x31,0X31,0x0A])
	print resp
	time.sleep(1)
	resp1 = spi.xfer([0x31,0x30,0x0A])
	print resp1
	time.sleep(1)
