import RPi.GPIO as GPIO
from time import sleep
import paho.mqtt.publish as publish
import sys

args = sys.argv

GPIO.setmode(GPIO.BCM)

# 1: pir_topic, 2: hostname, 3: pin

if len(args) > 3:
    pin = int(args[3])
else: 
    pin = 14

# GPIOの18を指定
# GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

print(str(pin) + "番で動作を検知します")
while True:
    sleep(1)

    # センサーが動体を検知するとPublishする
    if GPIO.input(pin) == GPIO.HIGH:
        publish.single(str(args[1]), str(1), hostname=str(args[2]))
    else:
        pass