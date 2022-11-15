import open3d as o3d
import numpy as np

def apriltag(path):
  pcd_at_bim = o3d.io.read_point_cloud(path)
  array = np.asarray(pcd_at_bim.points)
  num = int(len(array)/4)
  down_pcd_at_bim = pcd_at_bim.uniform_down_sample(num)
  o3d.io.write_point_cloud('apriltag.ply', down_pcd_at_bim, write_ascii=False)
