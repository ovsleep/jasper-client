# -*- coding: utf-8-*-
import requests
import re
import sys

WORDS = ["VER, PELICULAS, TELE, CABLE, XBOX, CHROME"]

def handle(text, mic, profile):
	url = "http://192.168.1.101:9589/api/remote"
	
	device = ''
	if bool(re.search(r'\bpeliculas\b', text, re.IGNORECASE)):
		device = 'pi'
	if bool(re.search(r'\btele\b', text, re.IGNORECASE)):
		device =  'tv'
	if bool(re.search(r'\bcable\b', text, re.IGNORECASE)):
		device =  'cable'
	if bool(re.search(r'\bxbox\b', text, re.IGNORECASE)):
		device =  'xbox'
	if bool(re.search(r'\bchrome\b', text, re.IGNORECASE)):
		device =  'chrome'

	action = { 'command': 'watch', 'data' : {'device': device} }
	requests.post(url, json=action)
		
def isValid(text):
	return bool(re.search(r'\bver\b', text, re.IGNORECASE))
