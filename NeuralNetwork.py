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
		percent = 0
		for item in range(0,len(output)):
			if (output[item] != round(self.classify(input[item]))):
				#plt.plot([input[item][0]], [input[item][1]], 'bo')
				#percent += 1
				percent +=1
			#else:
			#	percent +=1
				#plt.plot([input[item][0]], [input[item][1]], 'ro')
				#squaredError += 0.5*(output[item] - self.classify(input[item])) ** 2
		return percent/len(output)

	def backPropagation(self, input, output, training_rate):
		for i in range(0,len(input)):
			classification = self.classify(input[i])

			errorPerPair = (output[i] - classification)

			#For each synapse going from hidden to the single output node
			errorPerSynapse = []
			for j in range(0,len(self.nodesOutput[0].synapses)):
				#print("self.nodesOutput[0].value: ",self.nodesOutput[0].value)
				#print("sigmoidDeriv(self.nodesOutput[0].value): ",sigmoidDeriv(self.nodesOutput[0].value))
				errorPerSynapse.append(sigmoidDeriv(self.nodesOutput[0].value) * errorPerPair)

			#Hidden Layer
			errorHidden = []
			for node in self.nodesHidden:
				sum = 0.0
				for syn in range(0,len(node.synapses)):
					if node.synapses[syn].node_d is node:
						sum += node.synapses[syn].weight * sigmoidDeriv(node.synapses[syn].node_d.value) * errorPerPair
				errorHidden.append(sigmoidDeriv(node.value) * sum)
			#print(errorHidden)

			for node in self.nodesOutput:
				for syn in range(0,len(node.synapses)):
					if node.synapses[syn].node_d is node:
						#print("STARTING AT",node.synapses[syn].weight)
						adjustment = errorPerSynapse[syn] * node.synapses[syn].weight
						node.synapses[syn].weight -= training_rate * adjustment
						#print("CHANGED BY ",(training_rate * adjustment))


			# for h in range(0,len(self.nodesHidden)):
			# 	for o in range(0,len(self.nodesOutput)):
			# 		adjustment = errorPerSynapse[o] * self.nodesOutput[o].value

			# 		self.nodesOutput[o].value -= training_rate * adjustment

			for hNode in self.nodesHidden:
				for syn in range(0,len(hNode.synapses)):
					if hNode.synapses[syn].node_d is hNode:
						adjustment = errorHidden[syn] * hNode.synapses[syn].weight
						hNode.synapses[syn].weight -= training_rate * adjustment



			# for iNode in range(0,len(self.nodesInput)):
			# 	for hNode in range(0,len(self.nodesHidden)):
			# 		adjustment = errorHidden[hNode] * self.nodesInput[iNode].value

			# 		self.nodesInput[iNode].weight -= training_rate * adjustment
		#print()
		#plt.show()
		print(self.calculateError(input, output))
		return 