import logging
import RPi.GPIO as GPIO
import time

class Led:
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        GPIO.setup(24,GPIO.OUT)
        self.colors = {'RED':18, 'BLUE':23, 'GREEN':24}

    def switch(self, mode, color):
        pin = self.colors[color]
        GPIO.output(pin, mode)

    def blink(self, color, times=3):
        pin = self.colors[color]
        for i in range(times):
            time.sleep(0.3)
            GPIO.output(pin, True)
            time.sleep(0.3)
            GPIO.output(pin, False)