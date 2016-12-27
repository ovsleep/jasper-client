# -*- coding: utf-8-*-
import requests
import re
import sys

WORDS = ["AIRE, CALIENTE, FRIO, APAGAR"]

def handle(text, mic, profile):
	url = "http://192.168.1.101:9589/api/remote"
	
	if bool(re.search(r'\bapagar\b', text, re.IGNORECASE)):
		mode =  'off'
		action = { 'command': 'ac', 'data' : {'mode': mode} }
	else:
		mic.say('qué temperatura?')
		temp = mic.activeListen()
		
		if bool(re.search(r'\bcaliente\b', text, re.IGNORECASE)):
			mode =  'hot'
		else:
			mode = 'cold'
		
		action = { 'command': 'ac', 'data' : {'mode': mode, 'temp': temp} }
	requests.post(url, json=action)
		
def isValid(text):
	return bool(re.search(r'\baire\b', text, re.IGNORECASE))
