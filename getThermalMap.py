import time
import busio
import board
import csv
import os
import datetime

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

    if os.path.isdir('csv'):
        os.mkdir('csv')
    file = open(str(datetime.datetime.now()) + '.csv', 'w')
    w = csv.writer(file)

    i = 0
    while i < 100:
        max_temp = max(max(sensor.pixels))
        w.writerow(str(max_temp))
        print(str(i) + " : " + str(max_temp))
        i += 1

except KeyboardInterrupt:
    print("done")
