class data_point:	
	def __init__(self, x, y, label):
		self.x = x
		self.y = y
		self.label = label
		
	@property
	def x(self):
		return self._x
		
	@property
	def y(self):
		return self._y
		
	@property
	def label(self):
		return self._label
		
	@x.setter
	def x(self, value):
		self._x = value
		
	@y.setter
	def y(self, value):
		self._y = value
		
	@label.setter
	def label(self, value):
		self._label = value