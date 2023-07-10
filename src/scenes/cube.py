from shutil import get_terminal_size

import numpy as np

from src import transformations as trans
from src.scenes import Base


class Cube(Base):
    def __init__(self):
        self.count = 0

        w, h = get_terminal_size()

        self.length = 10
        self.start_x = round(w/2)
        self.start_y = 50
        self.start_z = round(h/2)

        self.center = np.array([round((x + self.length)/2) for x in (self.start_x, self.start_y, self.start_z)])

        self.only_draw_vertices = True
        

        temp = []
        for x in range(self.start_x, self.start_x + self.length +1):
            for y in range(self.start_y, self.start_y + self.length +1):
                for z in range(self.start_z, self.start_z + self.length +1):
                    if self.only_draw_vertices:
                        if x != self.start_x and x != self.start_x + self.length:
                            continue
                        if y != self.start_y and y != self.start_y + self.length:
                            continue
                        if z != self.start_z and z != self.start_z + self.length:
                            continue

                    temp.append([x, y, z])

        self.original_vertices = np.array(temp)
        self.vertices = np.array(temp)

        super().__init__()
        self.dump = True

    def tick(self):
        # faulty behavior to be resolved
        # delta = self.count % 50 - 25
        # self.vertices[:, 1] = [delta] * np.shape(self.vertices)[0]
        # self.count += 1
        c = self.count


        self.vertices = trans.rotateZ(self.original_vertices, self.count, self.center)
        if round(c) % 1 == 0:
            self.payload.append(self.vertices)

        # self.vertices = trans.rotateY(
        #     trans.rotateX(self.original_vertices, self.count, self.center),
        #     self.count,
        #     self.center)

        # vertices_2d = self.original_vertices[:, ::2].T
        # transformed_vertices_2d = np.matmul(rot_matrix, vertices_2d)
        # self.vertices[:, ::2] = transformed_vertices_2d.T

        self.count += 0.1
    
    # def __del__(self):
    #     import pickle
    #     with open('./data', mode='wb') as fp:
    #         pickle.dump(np.array(self.data), fp)
        
