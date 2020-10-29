# coding: utf-8
# Sample that outputs the value acquired by D6T.
# Please execute the following command before use "pigpio"
#  $ sudo pigpio

import grove_d6t
import pigpio
import time
import os
import numpy as np

# キャリブレーションするための補正値を読み込む
    calibrate_val = 0
    if os.path.isdir('conf') and os.path.exists('conf/calibration.txt'):
        with open('conf/calibration.txt', 'r') as f:
            calibrate_val = float(f.readline())

    print("calibrated: " + str(calibrate_val))

d6t = grove_d6t.GroveD6t()

while True:
    try:
        tpn, tptat = d6t.readData()
        if tpn is None:
            continue
        f = np.vectorize(lambda n, l=calibrate_val: n - l)
        thermal_map = f(tpn)
        print(thermal_map, "PTAT : %.1f" % tptat)
        time.sleep(1.0)
    except IOError:
        print("IOError")
