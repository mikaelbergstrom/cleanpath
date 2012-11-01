#!/usr/bin/python
import os, glob
sourcePath = "/Volumes/dmgskiva/Bil der/"
myFiles=[]

def scandirs(path):
	for currentFile in glob.glob( os.path.join(path, '*') ):
		if os.path.isdir(currentFile):
			scandirs(currentFile)
#		print currentFile
		myFiles.append(currentFile)

sourceFiles = scandirs(sourcePath)
print myFiles
print sourceFiles




