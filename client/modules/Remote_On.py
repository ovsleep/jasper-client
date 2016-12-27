# -*- coding: utf-8-*-
import requests
import re
import sys

WORDS = ["AIRE, CALIENTE, FRIO"]

def handle(text, mic, profile):
	url = "http://192.168.1.101:9589/api/remote"
	
	mic.say('qué temperatura?')
	temp = mic.activeListen()
	
	if bool(re.search(r'\bcaliente\b', text, re.IGNORECASE)):
		mode =  'hot'
	if bool(re.search(r'\bfrio\b', text, re.IGNORECASE)):
		mode = 'cold'
	
	action = { 'command': 'ac', 'data' : {'mode': mode, 'temp': temp} }
	requests.post(url, json=action)
		
def isValid(text):
	return bool(re.search(r'\bprender\b', text, re.IGNORECASE))
