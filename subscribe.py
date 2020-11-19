import paho.mqtt.subscribe as subscribe
import sys

# 1: Topoic, 2: hostname
args = sys.argv

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, str(message.payload.decode())))

while True:
    subscribe.callback(print_msg, str(args[1]), hostname=str(args[2]))