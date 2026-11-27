from common import TriMesh


def test_cons_one_tri():
	g = TriMesh()
	t = "T0" # label
	g.add_tri(t)
	assert g.degree[t] == 0
	assert not g.nodes[t]["refine"]
	g.assert_tri(t)

def test_compat_div():
	pass
