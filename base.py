class Rule:
	"""Abstract base class for rules. """

	def __init__(self, g, t):
		"""Creates an application attempt of a production for a given triangle 
		t and, possibly, for triangles related to triangle t. """
		self.g = g
		self.t = t

	@property
	def tri(self):
		"""Triangle data (refine flag + bonds + verts) for triangle t. """
		return self.g.nodes[self.t]

	def iff(self):
		"""Rule criteria, if satisfied the rule can be applied. """
		return NotImplemented

	def apply(self):
		"""Apply the rule. """
		return NotImplemented
