from shutil import get_terminal_size

import numpy as np

from src import transformations as trans
from src.scenes import Base


class Cube(Base):
    def __init__(self):
        super().__init__()
        self.count = 0

        w, h = get_terminal_size()

        self.length = 50
        self.start_x = round(w/2 - self.length/2)
        self.start_y = 20
        self.start_z = round(h/2 - self.length/2)

        self.center = np.array([round(x + self.length/2) for x in (self.start_x, self.start_y, self.start_z)])

        
        self.edges = [(0,1),(0,2),(3,1),(3,2),(0,4),(1,5),(2,6),(3,7),(4,5),(4,6),(7,5),(7,6)]

        temp = []

        for y in range(self.start_y, self.start_y + self.length +1):
            for x in range(self.start_x, self.start_x + self.length +1):
                for z in range(self.start_z, self.start_z + self.length +1):
                    c = 0
                    if x == self.start_x or x == self.start_x + self.length:
                        c += 1
                    if y == self.start_y or y == self.start_y + self.length:
                        c += 1
                    if z == self.start_z or z == self.start_z + self.length:
                        c += 1

                    if c < 3:
                        continue

                    temp.append([x, y, z])

        self.original_vertices = np.array(temp)
        self.vertices = np.array(temp)


    def tick(self):
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
        
