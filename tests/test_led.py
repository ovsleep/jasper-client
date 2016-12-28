import unittest
from client import led
import time

class TestLed(unittest.TestCase):

    @staticmethod
    def getLed(self):
        return led.Led()

    def testRed(self):
        led = getLed()
        led.switch(True, 'RED')
        time.sleep(3)
        led.switch(False, 'RED')

    def testBlue(self):
        led = getLed()
        led.switch(True, 'BLUE')
        time.sleep(3)
        led.switch(False, 'BLUE')

    def testGreen(self):
        led = getLed()
        led.switch(True, 'GREEN')
        time.sleep(3)
        led.switch(False, 'GREEN')