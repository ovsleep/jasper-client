import unittest
from client import led
import time

class TestLed(unittest.TestCase):

    def testRed(self):
        myLed = led.Led()
        myLed.switch(True, 'RED')
        time.sleep(3)
        myLed.switch(False, 'RED')

    def testBlue(self):
        myLed = led.Led()
        myLed.switch(True, 'BLUE')
        time.sleep(3)
        myLed.switch(False, 'BLUE')

    def testGreen(self):
        myLed = led.Led()
        myLed.switch(True, 'GREEN')
        time.sleep(3)
        myLed.switch(False, 'GREEN')