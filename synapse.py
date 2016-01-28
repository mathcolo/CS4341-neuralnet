#synapse.py

class Synapse:

	def __init__(self, weight, node_s, node_d):
		self.weight = weight
		self.node_d = node_d
		self.node_s = node_s
		
	@property
	def weight(self):
		return self._weight
		
	@property
	def node_d(self):
		return self._node_d

	@property
	def node_s(self):
	    return self._node_s	
		
	@weight.setter
	def weight(self, value):
		self._weight = value
		
	@node_d.setter
	def node_d(self, value):
		self._node_d = value

	@node_s.setter
	def node_s(self, value):
		self._node_s = value

	def __str__(self):
		return "Synapse(" + str(self.weight) + ", " + str(self.node_d) + ", " + str(self.node_s) + ")"

