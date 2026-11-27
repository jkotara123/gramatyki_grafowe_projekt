from base import Rule


class P0(Rule):
	@property
	def _compat_divisible(self):
		return self.g.compat_divisible(self.t)

	def iff(self):
		return self._compat_divisible and not self.tri["refine"]

	def apply(self):
		self.g.add_node(self.t, refine=True) # r: 0 -> 1
