from common import Tris, tris_vis_cp


if __name__ == "__main__":
	g = Tris()
	t0 = "T0" # label
	t1 = "T1" # label
	g.add_tri(t0)
	g.add_tri(t1)
	g.glue_tris(t0, 0, t1, 0)
	g.assert_tri(t0)
	g.assert_tri(t1)
	tris_vis_cp(g)
