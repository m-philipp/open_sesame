#!/usr/bin/env python

from flask import Flask

import RPi.GPIO as GPIO
import time
import threading

DEBUG = 1

OPEN_TIME = 2

GPIO.setmode(GPIO.BCM)
DOOR_IO = 25
GPIO.setup(DOOR_IO, GPIO.OUT)
GPIO.output(DOOR_IO, True) # Close the DOOR!


#  /home/pi/flaski/static/

class DoorOpener(threading.Thread): 
  def __init__(self): 
    threading.Thread.__init__(self) 
 
  def run(self): 
        GPIO.output(DOOR_IO, False)
        time.sleep(OPEN_TIME)
        GPIO.output(DOOR_IO, True)
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
	print "index.html delivery"
	return app.send_static_file('index.html')

@app.route("/open", methods=['POST'])
def open():
	print "opening door"
	DoorOpener().start()
	return "{success:true}"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int("80"))


#while True:
#        GPIO.output(DOOR_IO, True)
#        time.sleep(CHECK_FREQ)
#        GPIO.output(DOOR_IO, False)
#        time.sleep(CHECK_FREQ)

