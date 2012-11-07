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
	
def cleanDirectoryPaths(rootDirectory):
	for currentFile in glob.glob( os.path.join(rootDirectory, '*') ):
		if os.path.isdir(currentFile):
			print "---> renamed currentDir: " + currentFile + " to: " + cleanPath(currentFile)	
			os.rename(currentFile, cleanPath(currentFile))
			print "---> renamed OK!"
			cleanDirectoryPaths(cleanPath(currentFile))

def cleanPaths(rootDirectory):
	for currentFile in glob.glob( os.path.join(rootDirectory, '*') ):
		if os.path.isdir(currentFile):
			cleanPaths(currentFile)	
		print "---> renamed currentFile: " + currentFile + " to: " + cleanPath(currentFile)	
		os.rename(currentFile, cleanPath(currentFile))
		print "---> renamed OK!"

if __name__ == '__main__':
	# Mikaels root dir
	rootDirectory = '/Projects/cleanpath/scr/python/filenames/'
	# Kristers root dir
	# rootDirectory = '/Users/klaag/cleanpath/scr/python/filenames/'	
	
	# First only clean all directories
	cleanDirectoryPaths(rootDirectory)
	cleanPaths(rootDirectory)