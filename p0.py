def apply(g, tri):
	tri_data = g.nodes[tri]
	g.add_node(tri, refine=True) # r: 0 -> 1
