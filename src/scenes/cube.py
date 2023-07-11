from shutil import get_terminal_size

import numpy as np

from src import transformations as trans
from src.scenes import Base


class Cube(Base):
    def __init__(self):
        self.count = 0
        self.dump = False

        w, h = get_terminal_size()

        self.length = 50
        self.start_x = round(w/2 - self.length/2)
        self.start_y = 10
        self.start_z = round(h/2 - self.length/2)

        # honestly what the heck am i thinking
        self.center = np.array([round(x + self.length/2) for x in (self.start_x, self.start_y, self.start_z)])

        self.only_draw_vertices = False
        self.only_draw_border = True
        self.only_draw_face = True
        

        temp = []

        for x in range(self.start_x, self.start_x + self.length +1):
            for y in range(self.start_y, self.start_y + self.length +1):
                for z in range(self.start_z, self.start_z + self.length +1):
                    c = 0
                    if x == self.start_x or x == self.start_x + self.length:
                        c += 1
                    if y == self.start_y or y == self.start_y + self.length:
                        c += 1
                    if z == self.start_z or z == self.start_z + self.length:
                        c += 1

                    if self.only_draw_vertices and c < 3:
                        continue

                    if self.only_draw_border and c < 2:
                        continue

                    if self.only_draw_face and c < 1:
                        continue

                    temp.append([x, y, z])

        self.original_vertices = np.array(temp)
        self.vertices = np.array(temp)

        super().__init__()

    def tick(self):
        # faulty behavior to be resolved
        # delta = self.count % 50 - 25
        # self.vertices[:, 1] = [delta] * np.shape(self.vertices)[0]
        # self.count += 1
        c = self.count


        self.vertices = trans.rotateX(
        trans.rotateY(
            trans.rotateZ(self.original_vertices, self.count, self.center),
            self.count,
            self.center
        ),
        self.count,
        self.center
        )

        self.count += 0.1

        if not self.dump:
            return

        if round(c) % 1 == 0:
            self.payload.append(self.vertices)
        
