import time
import busio
import board
import cv2

import adafruit_amg88xx

import picamera
import picamera.array

import matplotlib.pyplot as plt

# I2Cバスの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)

try:
    # センサーの初期化
    sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)

    # センサーの初期化待ち
    time.sleep(.1)

    while True:
        max_temp = max(max(sensor.pixels))
        print("Max Temp: " + str(max_temp))

except KeyboardInterrupt:
    print("done")
