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
				synapse = Synapse(numpy.random.ranf(), node, thisNode)
				node.synapses.append(synapse)
				thisNode.synapses.append(synapse)


		for i in range(0,self.numOutput):
			thisNode = Node(Node.o)
			self.nodesOutput.append(thisNode)
			for node in self.nodesHidden:
				synapse = Synapse(numpy.random.ranf(), node, thisNode)
				node.synapses.append(synapse)
				thisNode.synapses.append(synapse)

	def classify(self, input):
		for i in range(0,len(input)):
			self.nodesInput[i].value = input[i]

		#Input to Hidden
		for node in self.nodesInput:
			for synapse in node.synapses:
				destination = synapse.node_d
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
			node.value = int(round(node.value))

		return node.value

	def backPropagation(self, input, output, training_rate):
		for i in range(0,len(input)):
			classification = self.classify(input[i])

			errorPerPair = output[i] - classification
			
			#For each synapse going from hidden to the single output node

			errorPerSynapse = []
			for j in range(0,len(self.nodesOutput[0].synapses)):
				errorPerSynapse.append(sigmoidDeriv(self.nodesOutput[0].value) * errorPerPair)

			#print(errorPerSynapse)

			#Hidden Layer

			errorHidden = []
			for node in self.nodesHidden:
				sum = 0.0
				for syn in range(0,len(node.synapses)):
					if node.synapses[syn].node_s is node:
						sum += node.synapses[syn].weight * errorPerSynapse[syn]
				errorHidden.append(sigmoidDeriv(node.value) * sum)
			#print(errorHidden)

			for h in range(0,len(self.nodesHidden)):
				for o in range(0,len(self.nodesOutput)):
					adjustment = errorPerSynapse[o] * self.nodesOutput[o].value

					self.nodesOutput[o].value -= training_rate * adjustment

			for iNode in range(0,len(self.nodesInput)):
				for hNode in range(0,len(self.nodesHidden)):
					adjustment = errorHidden[hNode] * self.nodesInput[iNode].value

					self.nodesInput[iNode].value -= training_rate * adjustment

			squaredError = 0.0
			percent = 0
			for item in range(0,len(output)):
				if (output[item] == self.classify(input[item])):
					plt.plot([input[item][0]], [input[item][1]], 'bo')
					percent += 1
				else:
					plt.plot([input[item][0]], [input[item][1]], 'ro')
				squaredError += 0.5*(output[item] - self.classify(input[item])) ** 2

			print(percent/len(input))
			plt.show()
				
			return squaredError