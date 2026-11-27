class Rule:
	"""Abstract base class for rules. """

	def __init__(self, g, tri):
		"""Creates an application attempt of a production for a given triangle 
		tri and, possibly, for triangles related to tri. """
		self.g = g
		self.tri = tri

	@property
	def tri_data(self):
		"""Triangle data (refine flag + bonds + verts) for tri. """
		return self.g.nodes[self.tri]

	def iff(self):
		"""Rule criteria, if satisfied the rule can be applied. """
		return NotImplemented

	def apply(self):
		"""Apply the rule. """
		return NotImplemented
