# -*- coding: utf-8-*-
import requests
import re
import sys
import unicodedata

def normalizeString(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

WORDS = ["CAMBIAR, FOX, DISCOVERY, HISTORY, DEPORTES, FOOTBALL, FX"]

def handle(text, mic, profile):
	url = "http://192.168.1.101:9589/api/remote"
	
	channel = re.search('(?<=cambiar )\w+', text, re.IGNORECASE | re.UNICODE).group(0)
	channel = normalizeString(channel);
	action = { 'command': 'change', 'data' : {'channel': channel} }
	requests.post(url, json=action)
		
def isValid(text):
	return bool(re.search(r'\bcambiar\b', text, re.IGNORECASE))

