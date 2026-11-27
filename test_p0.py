from test_common import VERT_POS, T0, T1, make_two_tris
from common import TriMesh
from p0 import P0



def test_p0_basic():
	g = make_two_tris()
	g.glue_tris(T0, 0, T1, 0)
	p = P0(g, T0)
	tri = g.nodes[T0]
	assert not tri["refine"]
	assert p.iff()
	p.apply()
	g.assert_tri(T0)
	tri = g.nodes[T0]
	assert tri["refine"]
	assert not p.iff()
