# -*- coding: utf-8-*-
import re
import sys

WORDS = ["QUIERO, MAS"]

def handle(text, mic, profile):
	mic.say('No se lo merece')
		
def isValid(text):
	return bool(re.search(r'\bquiero mas\b', text, re.IGNORECASE))
