#!/usr/bin/python
# encoding: UTF-8
import sys
import os, glob

myFiles=[]
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
	return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./_023456789"
	# return [a-z,A-Z,0-9]
	
	
def cleanPath(path):
    # Replace invalid characters
	cleanedPath = map(getReplaceChar, path)
    # Remove invalid characters 
	return ''.join(filter(isCharValid, cleanedPath))
	
def scandirs(fixedPath):
	for currentFile in glob.glob( os.path.join(fixedPath, '*') ):
		if os.path.isdir(currentFile):
			print "currentFileD:" + currentFile + ":" + cleanPath(currentFile)
			os.rename(currentFile, cleanPath(currentFile))
			scandirs(cleanPath(currentFile))
		myFiles.append(currentFile)
		if os.path.isdir(currentFile):
			print ""
		else:
			print "currentFile:" + currentFile + ":" + cleanPath(currentFile)
			os.rename(currentFile, cleanPath(currentFile))

if __name__ == '__main__':
	scandirs('/Users/klaag/cleanpath/scr/python/filenames/')
	#print('Cleaned Path: ' + cleanPath(getPath()))