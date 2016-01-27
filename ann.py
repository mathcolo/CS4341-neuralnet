# ann.py

import sys
import numpy
from data_point import *

def readFile(filename):
	input = []
	output = []
	
	try:
		with open(filename, 'r') as f:
			for line in f:
				data = line.split()
				input.append([data[0], data[1]])
				output.append(data[2])
	except FileNotFoundError as ex:
		print(filename, " could not be found.")
		exit()
	
	return input, output

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
	
layer = ['input', 'hidden', 'output']
list(enumerate(layer))

# get input into 3 variables	
filename, nodes, holdout = parseInput(sys.argv)

# create list of data point objects from file
input, output = readFile(filename)


print(input)

