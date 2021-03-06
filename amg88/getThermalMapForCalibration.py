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

        # センサーの初期化待ち
        time.sleep(.1)

        if not os.path.isdir('csv'):
            os.mkdir('csv')
        # 観測フォルダ番号を振る
        path = set_folder_name()

        file = open(path + 'temperature.csv', 'w')
        w = csv.writer(file)

        i = 0
        temp_ls = []
        while i < 100:
            max_temp = max(max(sensor.pixels))
            temp_ls.append(max_temp)
            w.writerow([str(max_temp)])
            print(str(i) + " : " + str(max_temp))
            i += 1

        file.close()
        with open(path + 'avg.txt', 'w') as f:
            f.write(str(sum(temp_ls) / len(temp_ls)))

        is_tmp = False
        temperature = 0
        while not is_tmp:
            print("Input your body temperature.")
            temp = input()
            try:
                float(temp)
                is_tmp = True
            except ValueError:
                pass
            temperature = float(temp)
        file = open(path + 'correct.csv', 'w')
        w = csv.writer(file)
        w.writerow([temperature])
        file.close()
        file = open(path + 'date.csv', 'w')
        w = csv.writer(file)
        w.writerow([str(datetime.datetime.now())])
        file.close()
        print("Result saved at " + path)
    except KeyboardInterrupt:
        print("done")


# csv以下の数値フォルダ名より今回のフォルダ名を振る&作る
def set_folder_name():
    ls = [0]
    for f in glob.glob('csv/*'):
        name = os.path.split(f)[1]
        if not name.isdecimal():
            pass
        ls.append(int(name))
    name = "{0:04d}".format(max(ls) + 1)
    os.mkdir('csv/' + name)
    return 'csv/' + name + '/'


if __name__ == "__main__":
    main()
