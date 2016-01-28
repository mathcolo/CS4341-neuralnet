# ann.py

import sys
import numpy
from node import *
from synapse import *

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

def sigmoid(input):
	#Function as taken from the textbook
	return 1/(1+numpy.exp(-1*input))

def sigmoidDeriv(input):
	return input * (1 - input);


layer = ['input', 'hidden', 'output']
list(enumerate(layer))

# get input into 3 variables	
filename, numHidden, holdout = parseInput(sys.argv)

# create list of data point objects from file
input, output = readFile(filename)
#print(input)

numInput = 2
#numHidden ^
numOutput = 1

nodesInput = []
for i in range(0,numInput):
	nodesInput.append(Node(Node.i))

nodesHidden = []
for i in range(0,numHidden):
	thisNode = Node(Node.h)
	nodesHidden.append(thisNode)
	for node in nodesInput:
		synapse = Synapse(numpy.random.ranf(), node, thisNode)
		node.synapses.append(synapse)
		thisNode.synapses.append(synapse)

nodesOutput = []
for i in range(0,numOutput):
	thisNode = Node(Node.o)
	nodesOutput.append(thisNode)
	for node in nodesHidden:
		synapse = Synapse(numpy.random.ranf(), node, thisNode)
		node.synapses.append(synapse)
		thisNode.synapses.append(synapse)

def classify(input, nodesInput, nodesHidden, nodesOutput):
	for i in range(0,len(input)):
		nodesInput[i].value = input[i]

	#Input to Hidden
	for node in nodesInput:
		for synapse in node.synapses:
			destination = synapse.node_d
			destination.value += node.value * synapse.weight
	
	#Hidden to Output
	for node in nodesHidden:
		node.value = sigmoid(node.value)

		for synapse in node.synapses:
			if synapse.node_s is node:
				destination = synapse.node_d
				destination.value += node.value * synapse.weight

	for node in nodesOutput:
		node.value = sigmoid(node.value)
		node.value = int(round(node.value))
		print(node)


def backPropagation(output, outputClassify, nodesInput, nodesHidden, nodesOutput):

	error = []
	for i in range(0, len(output)):
		error.append(output[i] - outputClassify[i])

	error = map(sigmoidDeriv, error)


	#Hidden Layer
	errorHidden = []
	for node in nodesHidden:
		for synapse in node.synapses:
			if synapse.node_s is node:
				





# for line in input:
# 	#print(line)
# 	classify(line, nodesInput, nodesHidden, nodesOutput)