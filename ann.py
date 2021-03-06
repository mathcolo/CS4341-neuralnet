# CS4341 Intro to AI (C16): Project 2
# Theresa Inzerillo and Preston Mueller
# February 1, 2016
# ann.py: driver/main file for the neural network project

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

	else:
		nodes = 5
		holdout = 20

		for i in range(0,len(args)):
			try:
				if str(args[i]) == "h":
					nodes = int(args[i+1])
					i += 1
				if str(args[i]) == "p":
					holdout = int(args[i+1])
					i += 1
			except:
				print("Invalid input")
				exit()

		if nodes < 0:
			print("Number of hidden nodes must be a non-negative integer.")
			exit()
		
		if holdout < 0 or holdout > 100:
			print("Holdout pecentage must be a non-negative integer.")
			exit()

	return args[1], nodes, holdout

# get input into 3 variables	
filename, numHidden, holdout = parseInput(sys.argv)

# create list of data point objects from file
input, output = readFile(filename)
#print(input)

numpy.random.seed(4)

numInput = 2
#numHidden ^
numOutput = 1

h_percent = holdout/100
h_num = int(round(len(input)*h_percent))

ann = NeuralNetwork(numInput, numHidden, numOutput)

ann.setup()

# run backprop to train the network with the training set
print("Running back propagation", end="",flush=True)
for x in range(0,5000):
	if x%100 is 0:
		print('.', end="",flush=True)
		#print(ann.backPropagation(input[0:h_num], output[0:h_num], .00000005))
	#else:

	ann.backPropagation(input[0:h_num], output[0:h_num], .00000005)
	
# test against rest of data
print("")
print(round(ann.calculateError(input[h_num+1:len(input)-1],output[h_num+1:len(output)-1])*100, 3), "% error")