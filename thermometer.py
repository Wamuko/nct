import time
import busio
import board
import cv2

import adafruit_amg88xx

import picamera
import picamera.array

import matplotlib.pyplot as plt

plt.ion()
plt.subplots(figsize=(8, 4))

# I2Cバスの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)

try:
    # センサーの初期化
    sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)

    # センサーの初期化待ち
    time.sleep(.1)

    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture('./tmp.jpg')

    max_temp = max(max(sensor.pixels))
    print(max_temp)
    img0 = cv2.imread('./tmp.jpg')
    img = img0[0:240, 41:280]
    img = img[:, :, ::-1].copy()

    plt.subplot(1, 2, 1)
    fig = plt.imshow(sensor.pixels, cmap="inferno", interpolation="bicubic", vmin=min(min(sensor.pixels)), vmax=max(max(sensor.pixels)))
    plt.colorbar()

    plt.subplot(1, 2, 2)
    plt.text(0, 0, str(max_temp) + 'deg', size=20, color="red")
    plt.savefig("img.png")

    plt.draw()

    plt.pause(0.03)
    plt.clf()

except KeyboardInterrupt:
    print("done")
