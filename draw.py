from common import norm
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.collections as pcl
import networkx as nx


def trimesh_vis_cp(g, pos=None, node_radius=1.0, bond_radius=0.2):
	node_style = {
		"edgecolor": "#000", "facecolor": "#fff"
	}
	bond_style = {
		"edgecolor": "#000", "facecolor": "#f22"
	}
	edge_style = {
		"edgecolor": "#000", "width": 0.5
	}
	if pos is None:
		pos = nx.spring_layout(g, seed=42)
	
	fig, ax = plt.subplots(figsize=(10, 7))
	
	def text(x, y, text):
		ax.text(
			x, y, text, 
			horizontalalignment='center', 
			verticalalignment='center'
		)


	for t, tri in g.nodes(data=True):
		x, y = pos[t]
		ax.add_patch(pat.Circle((x, y), node_radius, **node_style))
		refine = int(tri["refine"])
		text(x, y, f"{t}\nR={refine}")
	
	for t0, t1, edge in g.edges(data=True):
		x0, y0 = pos[t0]
		x1, y1 = pos[t1]
		dx, dy = x1 - x0, y1 - y0
		dlen = norm((x0, y0), (x1, y1))
		if dlen < 2*node_radius:
			# don't even bother if nodes are too close
			continue
		# move the arrow out of the circles
		px = dx / dlen * node_radius
		py = dy / dlen * node_radius	
		x0 += px
		y0 += py
		adx = dx - 2*px
		ady = dy - 2*py
		ax.add_patch(pat.Arrow(x0, y0, adx, ady, **edge_style))
		# bond
		x0 -= dx / dlen * bond_radius
		y0 -= dy / dlen * bond_radius
		ax.add_patch(pat.Circle((x0, y0), bond_radius, **bond_style))
		tri0 = g.nodes[t0]
		bond = tri0["bonds"][edge["from_bond"]]
		attrs = []
		if bond.refine_edge:
			attrs.append("RE")
		if bond.boundary:
			attrs.append("B")
		if bond.break_edge:
			attrs.append("BR")
		attrs_text = ",".join(attrs)
		text(x0, y0, f"{bond.b}\n{attrs_text}")


	ax.autoscale()
	plt.axis('equal')
	plt.show()
