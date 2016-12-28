import unittest
from client import led
import time

class TestLed(unittest.TestCase):

    def testRed(self):
        led = led.Led()
        led.switch(True, 'RED')
        time.sleep(3)
        led.switch(False, 'RED')

    def testBlue(self):
        led = led.Led()
        led.switch(True, 'BLUE')
        time.sleep(3)
        led.switch(False, 'BLUE')

    def testGreen(self):
        led = led.Led()
        led.switch(True, 'GREEN')
        time.sleep(3)
        led.switch(False, 'GREEN')