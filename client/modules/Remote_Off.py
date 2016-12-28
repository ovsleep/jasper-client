# -*- coding: utf-8-*-
import requests
import re
import sys

WORDS = ["APAGAR, TELE, AIRE, TODO, CHAU"]
PRIORITY = 100

def handle(text, mic, profile):
	url = "http://192.168.1.101:9589/api/remote"
	device = ''
	response = 'Muy bien, '

	if bool(re.search(r'\btele\b', text, re.IGNORECASE)):
		response += 'apago la tele'
		device =  'tv'
	if bool(re.search(r'\baire\b', text, re.IGNORECASE)):
		device =  'ac'
		response += 'apago el aire'
	if bool(re.search(r'\btodo\b', text, re.IGNORECASE)):
		response += 'adios!'
		device =  'all'
	if bool(re.search(r'\bchau\b', text, re.IGNORECASE)):
    	response += 'adios!'
		device = 'all'
		
	action = { 'command': 'off', 'data' : {'device': device} }
		
	requests.post(url, json=action)
	mic.say(response)
	
def isValid(text):
	print text
	return bool(re.search(r'\bapagar\b', text, re.IGNORECASE)) or bool(re.search(r'\bchau\b', text, re.IGNORECASE))
