class Rule:
	"""Abstract base class for rules. """
	def __init__(self, g, tri):
		self.g = g
		self.tri = tri

	@property
	def tri_data(self):
		return self.g.nodes[self.tri]

	def iff(self):
		return NotImplemented

	def apply(self):
		return NotImplemented
