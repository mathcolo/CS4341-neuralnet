class Node:	

	i = 1
	h = 2
	o = 3

	def __init__(self, fPtr, layer):
		self.fPtr = fPtr
		self.layer = layer
		
	@property
	def fPtr(self):
		return self._fPtr
		
	@property
	def layer(self):
		return self._layer
		
	@fPtr.setter
	def fPtr(self, value):
		self._fPtr = value
		
	@layer.setter
	def layer(self, value):
		self._layer = value

	def __str__(self):
		return "Node(" + str(self.fPtr) + ", " + str(self.layer) + ")"