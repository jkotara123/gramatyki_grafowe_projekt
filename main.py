from common import TriMesh
from draw import trimesh_vis_cp


T0 = "T0" # label
T1 = "T1" # label


if __name__ == "__main__":
	g = TriMesh()
	vert_pos = [(-1,-1), (0,+1),(+1,-1)]
	g.add_tri(T0, vert_pos)
	g.add_tri(T1, vert_pos)
	g.glue_tris(T0, 0, T1, 0)
	g.assert_tri(T0)
	g.assert_tri(T1)
	trimesh_vis_cp(g)
