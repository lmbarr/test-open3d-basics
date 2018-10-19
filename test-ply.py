import numpy as np
from open3d import *

if __name__ == "__main__":

    pcd = read_triangle_mesh("/Users/--/PycharmProjects/test-open3d/datos.ply")

    triangle_mesh = TriangleMesh()
    triangle_mesh.vertices = Vector3dVector([[0, 0, 0],
                              [0, 0, 1],
                              [0, 1, 1],
                              [0, 1, 0],
                              [1, 0, 0],
                              [1, 0, 1],
                              [1, 1, 1],
                              [1, 1, 0]])
    triangle_mesh.triangles = Vector3iVector([[1, 2, 3],
                                [6, 5, 4],
                                [4, 5, 1],
                                [5, 6, 2],
                                [6, 7, 3],
                                [7, 4, 0]])


    points = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0],
              [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    lines = [[0, 1], [0, 2], [1, 3], [2, 3],
             [4, 5], [4, 6], [5, 7], [6, 7],
             [0, 4], [1, 5], [2, 6], [3, 7]]
    colors = [[1, 0, 0] for i in range(len(lines))]

    line_set = LineSet()
    line_set.points = Vector3dVector(points)
    line_set.lines = Vector2iVector(lines)
    line_set.colors = Vector3dVector(colors)



    draw_geometries([triangle_mesh, line_set])
