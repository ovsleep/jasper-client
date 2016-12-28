# -*- coding: utf-8-*-
import re
from client import jasperpath

WORDS = ["SILENCIO", "HABLA"]


def handle(text, mic, profile):
    
    if bool(re.search(r'\bsilencio\b', text, re.IGNORECASE)):
        mic.say("Muy bien, no hablo más")
        mic.setSilentMode(True)
    else:
        mic.setSilentMode(False)
        mic.say("Recuperé mi voz!")

def isValid(text):
    return bool(re.search(r'\bsilencio\b', text, re.IGNORECASE)) or bool(re.search(r'\bhabla\b', text, re.IGNORECASE)) 
