#!/usr/bin/python
# encoding: UTF-8
import sys

# Need to check that lenght of file is never below 1 char.
	
charDict = { '1': '_', u'ö':'o' , u'Ö':'O' , u'å': 'a' , u'Å':'A' , u'ä':'a' , u'Ä':'A' }

def getPath():
	if len(sys.argv) > 1:
		return sys.argv[1].decode('utf-8')
	else:
		return raw_input('Please enter path:').decode('utf-8')
	
def getReplaceChar(char):
	if char in charDict.keys():
		return charDict[char]
	else:
		return char
		
def isCharValid(char):
	if char in getValidChars():
		return True
	else:
		return False		

def getValidChars():
	return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
	
def cleanPath(path):
    # Replace invalid characters
	cleanedPath = map(getReplaceChar, path)
    # Remove invalid characters 
	return ''.join(filter(isCharValid, cleanedPath))

if __name__ == '__main__':
	print('Cleaned Path: ' + cleanPath(getPath()))