# -*- coding: utf-8-*-
import requests
import re
import sys

WORDS = ["APAGAR, TELE, AIRE, TODO, CHAU"]

def handle(text, mic, profile):
	url = "http://192.168.1.101:9589/api/remote"
	device = ''

	if bool(re.search(r'\btele\b', text, re.IGNORECASE)):
		device =  'tv'
	if bool(re.search(r'\baire\b', text, re.IGNORECASE)):
		device =  'ac'
	if bool(re.search(r'\btodo\b', text, re.IGNORECASE)):
		device =  'all'
	if bool(re.search(r'\bchau\b', text, re.IGNORECASE)):
		device = 'all'
		
	action = { 'command': 'off', 'data' : {'device': device} }
		
	requests.post(url, json=action)
		
def isValid(text):
	return bool(re.search(r'\bapagar\b', text, re.IGNORECASE)) or bool(re.search(r'\bchau\b', text, re.IGNORECASE))
