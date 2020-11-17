import RPi.GPIO as GPIO
import sdf
import time
import datetime
import paho.mqtt.publish as publish
import sys

# 1: temperature_topic, 2: humidity_topic, 3: hostname
args = sys.argv

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = sdf.DHT11(pin=14)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            publish.single(str(args[1]), result.temperature, hostname=str(args[3]))
            publish.single(str(args[2]), result.humidity, hostname=str(args[3]))

        time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()