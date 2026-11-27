from common import TriMesh


T0 = "T0" # label
T1 = "T1" # label
VERT_POS = [(-1,-1), (0,+1), (+1,-1)]


def test_cons_one_tri():
	g = TriMesh()
	g.add_tri(T0, VERT_POS)
	assert g.degree[T0] == 0
	assert not g.nodes[T0]["refine"]
	g.assert_tri(T0)
	# TODO: test boundary bonds - maybe as a part of assert_tri()?

def make_two_tris() -> TriMesh:
	g = TriMesh()
	g.add_tri(T0, VERT_POS)
	g.add_tri(T1, VERT_POS)
	return g


def test_compat_div_refine_to_refine():
	g = make_two_tris()
	# glue the tris by the refinement edges
	g.glue_tris(T0, 0, T1, 0)
	assert g.compat_divisible(T0)
	assert g.compat_divisible(T1)


def test_compat_div_refine_to_boundary():
	g = make_two_tris()
	# mark T1/1 (bond 1) as boundary
	g.nodes[T1]["bonds"][1].boundary = True
	# glue the tris by the refinement edge and boundary edge
	g.glue_tris(T0, 0, T1, 1)
	assert g.compat_divisible(T0)
	assert not g.compat_divisible(T1)
