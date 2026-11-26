from common import Tris
import p0

def test_p0_apply():
	g = Tris()
	t = "T0" # label
	g.add_tri(t)
	p0.apply(g, t)
	g.assert_tri(t)
	t_data = g.nodes[t]
	assert t_data["refine"] == True
