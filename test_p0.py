from common import TriMesh
from p0 import P0


def test_p0():
	g = TriMesh()
	t = "T0" # label
	g.add_tri(t)
	p = P0(g, t)
	p.apply()
	g.assert_tri(t)
	t_data = g.nodes[t]
	assert t_data["refine"] == True
	assert not p.iff()
