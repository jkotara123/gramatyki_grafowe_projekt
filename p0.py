from base import Rule


class P0(Rule):
	def iff(self):
		# TODO: For now, let's assume the tri was already checked with 
		# compat_divisible()
		return not self.tri_data["refine"]

	def apply(self):
		self.g.add_node(self.tri, refine=True) # r: 0 -> 1
