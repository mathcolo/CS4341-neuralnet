# ann.py

import sys
import numpy
from data_point import *

def readFileToDataPoint(filename):
	datalist = []
	
	try:
		with open(filename, 'r') as f:
			for line in f:
				input = line.split()
				datalist.append(data_point(input[0], input[1], input[2]))
	except FileNotFoundError as ex:
		print(filename, " could not be found.")
		exit()
	
	return datalist

def parseInput(args):
	if len(args) is 2:
		print("test")
		return args[1], 5, 20

	elif len(args) is 4:
		try:
			nodes = int(args[2])
		except ValueError as ex:
			print("error: ", args[2], " is not a valid integer.")
			exit()
			
		try:
			holdout = int(args[3])
		except ValueError as ex:
			print("error: ", args[3], " is not a valid integer.")
			exit()

		if nodes < 0:
			print("Number of hidden nodes must be a non-negative integer.")
		
		if holdout < 0 or holdout > 100:
			print("Holdout pecentage must be a non-negative integer.")		
	else:
		print("Incorrect usage. Proper usage is python file.txt [ nodes | holdout percentage ]")
	
	return args[1], nodes, holdout

def sigmoidFunction(output):
	return 0
	

# get input into 3 variables	
filename, nodes, holdout = parseInput(sys.argv)

# create list of data point objects from file
data = readFileToDataPoint(filename)

