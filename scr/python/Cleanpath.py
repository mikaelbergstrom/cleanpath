#!/usr/bin/python
# encoding: UTF-8

#Testcomment
	
charDict = { '1': '_', u'ö':'o' , u'Ö':'O' , u'å': 'a' , u'Å':'A' , u'ä':'a' , u'Ä':'A' }

def getPath():
	return u"/Volumes/Data/2öfile1.jpg"
	
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
	cleanedPath = map(getReplaceChar, path)
    # Remove unicode 
	return ''.join(filter(isCharValid, cleanedPath))

if __name__ == '__main__':
	print( "Cleaned Path: " + cleanInvalidPath() )
