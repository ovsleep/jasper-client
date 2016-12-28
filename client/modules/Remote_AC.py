# -*- coding: utf-8-*-
import requests
import re
import sys
import logging

WORDS = ["AIRE, CALIENTE, FRIO, APAGAR"]

def handle(text, mic, profile):
	url = "http://192.168.1.101:9589/api/remote"
	response = 'Muy bien, '

	if bool(re.search(r'\bapagar\b', text, re.IGNORECASE)):
		mode =  'off'
		action = { 'command': 'ac', 'data' : {'mode': mode} }
		response += 'apago el aire'

	else:
		mic.say('qué temperatura?')
		temp = mic.activeListen()
		
		if bool(re.search(r'\bcaliente\b', text, re.IGNORECASE)):
			mode =  'hot'
			response += 'aire caliente a '		
		else:
			mode = 'cold'
			response += 'aire frío a '

		action = { 'command': 'ac', 'data' : {'mode': mode, 'temp': temp} }

	requests.post(url, json=action)
	mic.say(response + `temp` + ' grados')
	# mic.say(temp)
	# mic.say('grados')
		
def isValid(text):
	return bool(re.search(r'\baire\b', text, re.IGNORECASE))
