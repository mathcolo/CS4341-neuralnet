# CS4341 Intro to AI (C16): Project 2
# Theresa Inzerillo and Preston Mueller
# February 1, 2016
# node.py: node class for the neural net

class Node:	

	i = 1
	h = 2
	o = 3

	def __init__(self, layer):
		self.synapses = []
		self.layer = layer
		self.value = 0.0
		
	@property
	def synapses(self):
		return self._synapses
		
	@property
	def layer(self):
		return self._layer

	@property
	def value(self):
	    return self._value	
		
	@synapses.setter
	def synapses(self, value):
		self._synapses = value
		
	@layer.setter
	def layer(self, value):
		self._layer = value

	@value.setter
	def value(self, value):
		self._value = value

	def __str__(self):
		return "Node(" + str(self.layer) + ", " + str(self.value) + ")"