# ann.py

import sys
import numpy
from node import *
from synapse import *
from NeuralNetwork import *

def readFile(filename):
	input = []
	output = []
	
	try:
		with open(filename, 'r') as f:
			for line in f:
				data = line.split()
				input.append([float(data[0]), float(data[1])])
				output.append(float(data[2]))
	except FileNotFoundError as ex:
		print(filename, " could not be found.")
		sys.exit()
	
	return input, output

def parseInput(args):
	if len(args) is 2:
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
		sys.exit()
	
	return args[1], nodes, holdout

# get input into 3 variables	
filename, numHidden, holdout = parseInput(sys.argv)

# create list of data point objects from file
input, output = readFile(filename)
#print(input)

numInput = 2
#numHidden ^
numOutput = 1

h_percent = holdout/100
h_num = int(round(len(input)*h_percent))

ann = NeuralNetwork(numInput, numHidden, numOutput)

ann.setup()

# run backprop to train the network with the training set
for x in range(0,2000):
	ann.backPropagation(input[0:h_num], output[0:h_num], .001)
	
# test against rest of data
print(round(ann.calculateError(input[h_num+1:len(input)-1],output[h_num+1:len(output)-1])*100, 3), "% error")
	
	

# for line in input:
# 	#print(line)
# 	classify(line, nodesInput, nodesHidden, nodesOutput)