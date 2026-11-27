from base import Rule


class P0(Rule):
	@property
	def _compat_divisible(self):
		return self.g.compat_divisible(self.tri)

	def iff(self):
		return self._compat_divisible and not self.tri_data["refine"]

	def apply(self):
		self.g.add_node(self.tri, refine=True) # r: 0 -> 1
