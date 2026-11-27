from math import sqrt
import networkx as nx
import matplotlib.pyplot as plt
# Rules
from p0 import P0


def norm(point0, point1):
	x0, y0 = point0
	x1, y1 = point1
	dx, dy = x0 - x1, y0 - y1
	return sqrt(dx*dx + dy*dy)


class Bond:
	"""CP-graph bond. Index in triangle is indicated by the b field. """
	def __init__(self, b, refine_edge=False, boundary=False, break_edge=False):
		self.b = b
		self.refine_edge = refine_edge
		self.boundary = boundary
		self.break_edge = break_edge


class TriMesh(nx.DiGraph):
	"""Badly implemented representation of the CP-graph. """
	# TODO: properly mark bonds as boundary

	def __init__(self):
		"""Initalize empty CP-graph with an empty compatible stack. """
		super().__init__() # initialize the parent class
		self.compat_stack = [] # compatible triangles stack

	def add_tri(self, tri, vert_pos):
		"""Add new triangle. Vertex positions should consist of 3 coord pairs: 
		`[(x0,y0), (x1,y1), (x2,y2)]`. """
		assert len(vert_pos) == 3
		self.add_node(
			tri, 
			refine=False, # mark for refinement
			# TODO: maybe pick the longest edge and not just the first?
			# (see "Newest Vertex Bisection of Triangles Algorithm" page 7)
			bonds=[Bond(0, refine_edge=True), Bond(1), Bond(2)], # bonds
			verts=vert_pos # vertex positions
		)

	def glue_tris(self, t0, b0, t1, b1):
		"""Glue two triangles to each other, forming an edge. """
		# TODO: handle vertex positions?
		self.add_edge(
			t0, t1,
			from_bond=b0, to_bond=b1
		)
		self.add_edge(
			t1, t0,
			from_bond=b1, to_bond=b0
		)

	def neigh(self, t, b):
		"""Get neighbour of the triangle at bond index - return neighbouring
		triangle key and its bond index, which this triangle is connected to.
		If this bond is not connected anywhwere, return None pair. """
		for neigh_tri, edge in self.adj[t].items():
			if edge["from_bond"] == b:
				return neigh_tri, edge["to_bond"]

		return None, None

	def vert_pos(self, t, b):
		"""Get vertex positions for the given bond (triangle edge). """
		tri = self.nodes[t]
		v0 = b
		v1 = b + 1
		if v1 > 2:
			v1 -= 2
		verts = tri["verts"]
		return verts[v0], verts[v1]

	def peak_opposite(self, t):
		"""Obtain edge that is opposite to the peak vertex. """
		tri = self.nodes[t]
		# find refinement edge
		for bond in tri["bonds"]:
			if bond.refine_edge:
				return bond.b

		return None

	def compat_divisible(self, t):
		"""Test if triangle is compatibly divisible. """
		# find refinement edge
		refine_edge_b = self.peak_opposite(t)
		# no refinement edge found
		if refine_edge_b is None:
			return False
		# get adjacent triangle for that edge
		neigh_t, neigh_b = self.neigh(t, refine_edge_b)
		# no neighbour - not a refinement edge
		if neigh_t is None:
			return False
		neigh_tri = self.nodes[neigh_t]
		neigh_bond = neigh_tri["bonds"][neigh_b]
		return neigh_bond.boundary or neigh_bond.refine_edge

	def refine(self, t):
		"""Try refining the triangle mesh. """
		b = self.peak_opposite(t)
		po_t, _ = self.neigh(t, b)
		if not self.compat_divisible(t):
			# fingers crossed it doesn't loop forever
			self.refine(po_t)
		else:
			# apply rule P0
			p = P0(self, t)
			if p.iff(): p.apply()

	def assert_tri(self, t):
		"""Assert that the triangle is valid. """
		# Check if not too many edges are connected
		assert self.degree[t] <= 3
		# Check triangle data integrity
		tri = self.nodes[t]
		bonds = tri["bonds"]
		assert len(bonds) == 3
		# Check if there is one and only one refinement edge
		refine_edge_cnt = sum(
			bond.refine_edge 
			for bond in bonds
		)
		assert refine_edge_cnt == 1


def tris_vis_cp(g, pos=None):
	if pos is None:
		pos = nx.spring_layout(g, seed=42)
	
	nodes = [

	]
	fig, ax = plt.subplots(figsize=(10, 7))
	nx.draw_networkx_nodes()
	plt.show()
