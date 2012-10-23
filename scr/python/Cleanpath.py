#!/usr/bin/python
# encoding: UTF-8

def getValidChars():
	# Input is an environment to match.
	"""Indata Mac, Win, Unix"""

	return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
	
"""
def getValidChars(env)
	if env == 'Mac':
		return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
	elif env == 'Win':
		return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
	elif env == 'Unix':
		return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./"
	else
		return "abcABC"
"""
charDict = { '1': '_', u'ö':'o' , u'Ö':'O' , u'å': 'a' , u'Å':'A' , u'ä':'a' , u'Ä':'A' }


def getReplaceChar(char):
	# Input is a character
	"""Indata Mac, Win, Unix"""
	# List of characters to replace
	# If incoming char is in list, return replacement character, if not return empty string, effectivly removing it.
	#print( "Dictcheck of:" + char)
	if char in charDict.keys():
	#	print( "foundKey:" + charDict[char] )
		return charDict[char]
	else:
		return char
	
def getPath():
	# Get path(s) of file(s) to examine
	return u"/Volumes/Data/2öfile1.jpg"

def cleanInvalidPath(path):
	newPath=""
	validChars = getValidChars()
	for char in path:
		print( "newPath:" + newPath )
		if validChars.find(char) == -1:
			print( "invalidfound: " + char )
			newPath += getReplaceChar(char)
		else:
			newPath += char
	return newPath
#print( getReplaceChar('ö') )

def validChar(char):
	if char in getValidChars():
		return True
	else:
		return False
		
def even(number):
	if number % 2 == 0:
		return True
	else:
		return False

#filter(Cleanpath.validChar,''.join(map(Cleanpath.getReplaceChar,Cleanpath.getPath())))

if __name__ == '__main__':
	print( "Cleaned Path: " + cleanInvalidPath() )
