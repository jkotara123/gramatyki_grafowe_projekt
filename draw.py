from common import norm
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.collections as pcl
import networkx as nx


def trimesh_vis_cp(g, pos=None, node_radius=1):
	if pos is None:
		pos = nx.spring_layout(g, seed=42)
	
	fig, ax = plt.subplots(figsize=(10, 7))
	for t, tri in g.nodes(data=True):
		x, y = pos[t]
		ax.add_patch(pat.Circle((x, y), node_radius))
		ax.text(x, y, t)
	
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
		dx -= 2*px
		dy -= 2*py
		ax.add_patch(pat.Arrow(x0, y0, dx, dy))

	ax.autoscale()
	plt.axis('equal')
	plt.show()
