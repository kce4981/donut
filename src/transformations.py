import numpy as np

def rotate_matrix(radian) -> np.array:
    return [
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)]
    ]

def scale_matrix(k, h, j) -> np.array:
    return np.array([
        [k, 0, 0],
        [0, h, 0],
        [0, 0, j]
    ])


def rotateX(vertices: np.array, radian: float, origin=np.array([0,0,0])) -> np.array:

    vertices_copy =  vertices - origin

    vert_2d = vertices_copy[:, 1:].T
    multiplied_vert_2d = np.matmul(rotate_matrix(radian), vert_2d).T
    new_vertices = vertices_copy.copy()
    new_vertices[:, 1:] = multiplied_vert_2d

    new_vertices += origin

    return new_vertices

def rotateY(vertices: np.array, radian: float, origin=np.array([0,0,0])) -> np.array:

    vertices_copy =  vertices - origin

    vert_2d = vertices_copy[:, ::2].T
    multiplied_vert_2d = np.matmul(rotate_matrix(radian), vert_2d).T
    new_vertices = vertices_copy.copy()
    new_vertices[:, ::2] = multiplied_vert_2d

    new_vertices += origin

    return new_vertices

def rotateZ(vertices: np.array, radian: float, origin=np.array([0,0,0])) -> np.array:

    vertices_copy =  vertices - origin

    vert_2d = vertices_copy[:, :2].T
    multiplied_vert_2d = np.matmul(rotate_matrix(radian), vert_2d).T
    new_vertices = vertices_copy.copy()
    new_vertices[:, :2] = multiplied_vert_2d

    new_vertices += origin

    return new_vertices
