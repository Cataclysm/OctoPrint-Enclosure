import sys
import time

import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

if len(sys.argv) == 8:
    SPI_PORT = int(sys.argv[1])
    SPI_DEVICE = int(sys.argv[2])
    LED_COUNT = int(sys.argv[3])
    LED_BRIGHTNESS = int(sys.argv[4])
    red = int(sys.argv[5])
    green = int(sys.argv[6])
    blue = int(sys.argv[7])
else:
    print("fail")
    sys.exit(1)

pixels = Adafruit_WS2801.WS2801Pixels(LED_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)
color = Adafruit_WS2801.RGB_to_color(red, green, blue)

for i in range(pixels.count()):
    pixels.set_pixel(i, color)

pixels.show()

print("ok")
