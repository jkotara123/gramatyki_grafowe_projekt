import networkx as nx
import matplotlib.pyplot as plt
# Rules
import p0


class Bond:
	def __init__(self, i, refine_edge=False, boundary=False, break_edge=False):
		self.i = i
		self.refine_edge = refine_edge
		self.boundary = boundary
		self.break_edge = break_edge


class Tris(nx.DiGraph):
	"""Badly implemented representation of the CP-graph. """

	def add_tri(self, tri):
		"""Add new triangle. """
		self.add_node(
			tri, 
			refine=False, # mark for refinement
			# TODO: maybe pick the longest edge and not just the first?
			# (see "Newest Vertex Bisection of Triangles Algorithm" page 7)
			bonds=[Bond(0, refine_edge=True), Bond(1), Bond(2)] # bonds
		)

	def glue_tris(self, tri_a, bond_a, tri_b, bond_b):
		"""Glue two triangles to each other, forming an edge. """
		self.add_edge(
			tri_a, tri_b,
			from_bond=bond_a, to_bond=bond_b
		)
		self.add_edge(
			tri_b, tri_a,
			from_bond=bond_b, to_bond=bond_a
		)

	def neigh(self, tri, bond):
		"""Get neighbour of the triangle at bond index - return neighbouring
		triangle key and its bond index, which this triangle is connected to.
		If this bond is not connected anywhwere, return None pair. """
		for neigh_tri, edge in self.adj[tri].items():
			if edge["from_bond"] == bond:
				return neigh_tri, edge["to_bond"]

		return None, None

	def peak_opposite(self, tri):
		tri_data = self.nodes[tri]
		# find refinement edge
		for bond_data in tri_data["bonds"]:
			if bond_data.refine_edge:
				return bond_data.i

		return None

	def compat_divisible(self, tri):
		"""Test if triangle is compatibly divisible. """
		# find refinement edge
		refine_edge_bond = self.peak_opposite(tri)
		# no refinement edge found
		if refine_edge_bond is None:
			return False
		# get adjacent triangle for that edge
		neigh_tri, neigh_bond = self.neigh(tri, refine_edge_bond)
		neigh_tri_data = self.nodes[neigh_tri]
		neigh_bond_data = neigh_tri_data["bonds"][neigh_bond]
		return neigh_bond_data.boundary or neigh_bond_data.refine_edge

	def refine(self, tri):
		bond = self.peak_opposite(tri)
		po_tri, _ = self.neigh(tri, bond)
		if not self.compat_divisible(tri):
			# fingers crossed it doesn't loop forever
			self.refine(po_tri)
		else:
			# apply rule P0
			p0.apply(self, tri)

	def assert_tri(self, tri):
		"""Assert that the triangle is valid. """
		# Check if not too many edges are connected
		assert self.degree[tri] <= 3
		# Check triangle data integrity
		tri_data = self.nodes[tri]
		bonds = tri_data["bonds"]
		assert len(bonds) == 3
		# Check if there is one and only one refinement edge
		refine_edge_cnt = sum(
			bond_data.refine_edge 
			for bond_data in bonds
		)
		assert refine_edge_cnt == 1


def tris_vis_cp(g, **kwargs):
	nx.draw_planar(g, with_labels=True, **kwargs)
	plt.show()
