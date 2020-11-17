import time
import cv2
import matplotlib.pyplot as plt

plt.ion()
plt.subplots(figsize=(8, 4))


try:
    pixels = [[23.75, 23.0, 21.5, 21.75, 21.0, 20.75, 20.75, 21.25], [21.5, 21.0, 21.25, 21.5, 21.25, 21.0, 21.5, 21.0], [21.75, 22.75, 23.75, 22.75, 21.0, 21.25, 21.0, 21.0], [22.0, 23.25, 25.0, 26.25, 21.0, 20.0, 21.25, 21.25], [22.25, 22.75, 26.5, 28.25, 22.75, 20.0, 21.25, 21.75], [22.0, 22.5, 24.5, 28.25, 24.0, 21.0, 21.5, 21.5], [22.5, 24.75, 25.75, 26.75, 25.5, 25.0, 23.75, 22.5], [24.0, 24.75, 24.75, 25.25, 25.5, 25.5, 27.75, 24.0]]

    img0 = cv2.imread('tmp.jpg')
    img = img0[0:240, 41:280]
    img = img[:, :, ::-1].copy()

    plt.subplot(1, 2, 1)
    plt.imshow(pixels, cmap="inferno", interpolation="bicubic", vmin=min(min(pixels)), vmax=max(max(pixels)))
    plt.colorbar()

    plt.subplot(1, 2, 2)
    plt.imshow(img)
    plt.text(0, 0, "最高表面温度" + str(max(max(pixels))) + 'deg', size=20, color="red")
    plt.savefig("img.png")

    plt.draw()

    plt.pause(0.01)
    plt.clf()

except KeyboardInterrupt:
    print("done")