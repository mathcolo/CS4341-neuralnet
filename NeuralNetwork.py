# CS4341 Intro to AI (C16): Project 2
# Theresa Inzerillo and Preston Mueller
# February 1, 2016
# NeuralNetwork.py: core of the neural net

from node import *
from synapse import *
import numpy
import matplotlib.pyplot as plt

def sigmoid(input):
	#Function as taken from the textbook
	return 1/(1 + numpy.exp(-1 * input))

def sigmoidDeriv(input):
	return input * (1 - input);

class NeuralNetwork:	
	nodesInput = []
	nodesHidden = []
	nodesOutput = []

	def __init__(self, numInput, numHidden, numOutput):
		self.numInput = numInput
		self.numHidden = numHidden
		self.numOutput = numOutput

	def setup(self):
		for i in range(0,self.numInput):
			self.nodesInput.append(Node(Node.i))

		for i in range(0,self.numHidden):
			thisNode = Node(Node.h)
			self.nodesHidden.append(thisNode)
			for node in self.nodesInput:
				synapse = Synapse((numpy.random.ranf()*2)-1, node, thisNode)
				node.synapses.append(synapse)
				thisNode.synapses.append(synapse)


		for i in range(0,self.numOutput):
			thisNode = Node(Node.o)
			self.nodesOutput.append(thisNode)
			for node in self.nodesHidden:
				synapse = Synapse((numpy.random.ranf()*2)-1, node, thisNode)
				node.synapses.append(synapse)
				thisNode.synapses.append(synapse)

	def classify(self, input):

		self.resetNodes()

		for i in range(0,len(input)):
			self.nodesInput[i].value = input[i]

		#Input to Hidden
		for node in self.nodesInput:
			for synapse in node.synapses:
				destination = synapse.node_d #A hidden node
				destination.value += node.value * synapse.weight
		
		#Hidden to Output
		for node in self.nodesHidden:
			node.value = sigmoid(node.value)

			for synapse in node.synapses:
				if synapse.node_s is node:
					destination = synapse.node_d
					destination.value += node.value * synapse.weight

		for node in self.nodesOutput:
			node.value = sigmoid(node.value)
			#node.value = round(node.value)

		return node.value

	def resetNodes(self):
		for node in self.nodesInput:
			node.value = 0.0

		for node in self.nodesHidden:
			node.value = 0.0

		for node in self.nodesOutput:
			node.value = 0.0
			
	def calculateError(self, input, output):
		squaredError = 0.0
		for item in range(0,len(output)):
			squaredError += 0.5*(output[item] - self.classify(input[item])) ** 2
		return squaredError/len(output)

	def backPropagation(self, input, output, training_rate):
		for i in range(0,len(input)):
			classification = int(round(self.classify(input[i])))

			errorPerPair = (output[i] - classification)*-1

			#For each synapse going from hidden to the single output node
			errorPerSynapse = []
			for node in self.nodesOutput:
				for j in range(0,len(node.synapses)):
					errorPerSynapse.append(sigmoidDeriv(node.value) * errorPerPair)

			errorHidden = []
			for node in self.nodesHidden:
				sum = 0.0
				for syn in range(0,len(node.synapses)):
					if node.synapses[syn].node_d is node:
						sum += node.synapses[syn].weight * errorPerPair
				errorHidden.append(sigmoidDeriv(node.value) * sum)

			for node in self.nodesOutput:
				for syn in range(0,len(node.synapses)):
					adjustment = errorPerSynapse[syn] * node.synapses[syn].weight
					node.synapses[syn].weight -= training_rate * adjustment

			for hNode in self.nodesHidden:
				for syn in range(0,len(hNode.synapses)):
					if hNode.synapses[syn].node_d is hNode:
						adjustment = errorHidden[syn] * hNode.synapses[syn].weight
						hNode.synapses[syn].weight -= training_rate * adjustment
			
		return self.calculateError(input, output)
		

		
	def printNetwork(self):

		print("Left Synapses:")
		for node in self.nodesHidden:
				for syn in range(0,len(node.synapses)):
					if node.synapses[syn].node_d is node:
						print(node.synapses[syn])

		print("Right Synapses:")
		for node in self.nodesOutput:
				for syn in range(0,len(node.synapses)):
						print(node.synapses[syn])