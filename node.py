class Node:	
	def __init__(self, fPtr, bPtr, layer):
		self.fPtr = fPtr
		self.bPtr = bPtr
		self.layer = layer
		
	@property
	def fPtr(self):
		return self._fPtr
		
	@property
	def bPtr(self):
		return self._bPtr
		
	@property
	def layer(self):
		return self._layer
		
	@fPtr.setter
	def fPtr(self, value):
		self._fPtr = value
		
	@bPtr.setter
	def bPtr(self, value):
		self._bPtr = value
		
	@layer.setter
	def layer(self, value):
		self._layer = value