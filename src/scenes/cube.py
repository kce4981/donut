import numpy as np

class Cube:
    def __init__(self):
        self.count = 0
        temp = []
        # temp.append([10, 10, 10])
        # temp.append([30, 10, 10])
        # temp.append([10, 10, 30])
        # temp.append([30, 10, 30])

        for z in range(10, 31):
            for x in range(10, 31):
                for y in range(10, 16):
                    if z != 10 and z != 30:
                        continue
                    if x != 10 and x != 30:
                        continue
                    if y != 10 and y != 15:
                        continue

                    temp.append([x, y, z])

        self.original_vertices = np.array(temp)
        self.vertices = np.array(temp)

    def tick(self):
        # faulty behavior to be resolved
        # delta = self.count % 50 - 25
        # self.vertices[:, 1] = [delta] * np.shape(self.vertices)[0]
        # self.count += 1
        c = self.count

        # rotates against the origin

        rot_matrix = [
            [np.cos(c), -np.sin(c)],
            [np.sin(c), np.cos(c)]
        ]

        vertices_2d = self.original_vertices[:, ::2].T
        transformed_vertices_2d = np.matmul(rot_matrix, vertices_2d)
        self.vertices[:, ::2] = transformed_vertices_2d.T

        self.count += 0.1
        
