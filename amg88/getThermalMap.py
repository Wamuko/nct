import time
import busio
import board
import csv
import os
import datetime
import glob

import adafruit_amg88xx

import picamera
import picamera.array

import matplotlib.pyplot as plt


def main():
    # I2Cバスの初期化
    i2c_bus = busio.I2C(board.SCL, board.SDA)

    try:
        # センサーの初期化
        sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)
        calibrate_val = 0
        if os.path.isdir('conf') and os.path.exists('conf/calibration.txt'):
            with open('conf/calibration.txt', 'r') as f:
                calibrate_val = float(f.readline())
        # センサーの初期化待ち
        time.sleep(.1)

        while True:
            thermal_map = map(lambda n, l=calibrate_val: n - l, sensor.pixels)
            print(thermal_map)

    except KeyboardInterrupt:
        print("done")


if __name__ == "__main__":
    main()
