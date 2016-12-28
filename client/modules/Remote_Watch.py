# -*- coding: utf-8-*-
import requests
import re
import sys

WORDS = ["VER, PELICULAS, TELE, CABLE, XBOX, CHROME"]

def handle(text, mic, profile):
    text = text.encode('utf8')
	print text

	url = "http://192.168.1.101:9589/api/remote"
	response = 'Ok, '
	device = ''
	if bool(re.search(r'\bpeliculas\b', text, re.IGNORECASE)):
		device = 'pi'
		response += ' prendo la PI'
	if bool(re.search(r'\btele\b', text, re.IGNORECASE)):
		device =  'tv'
		response += ' pongo la TV'
	if bool(re.search(r'\bcable\b', text, re.IGNORECASE)):
		device =  'cable'
		response += ' prendo el cable'		
	if bool(re.search(r'\bxbox\b', text, re.IGNORECASE)):
		device =  'xbox'
		response += ' pongo la x box'				
	if bool(re.search(r'\bchrome\b', text, re.IGNORECASE)):
		device =  'chrome'
		response += ' pongo el crom cast'		
		
	action = { 'command': 'watch', 'data' : {'device': device} }
	requests.post(url, json=action)
	mic.say(response.encode('utf8'))

def isValid(text):
    text = text.encode('utf8')
	return bool(re.search(r'\bver\b', text, re.IGNORECASE))
