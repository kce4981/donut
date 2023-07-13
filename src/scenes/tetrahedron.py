import numpy as np
from shutil import get_terminal_size

from src.scenes import Base
from src import transformations as trans

class Tetrahedron(Base):

    def __init__(self) -> None:
        super().__init__()

        self.edges = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
        self.radian = 0

        w, h = get_terminal_size()

        self.length = 40
        ln = self.length
        self.center = [w/2, 20, h/2]

        temp = []
        temp.append([0,0,-ln])
        temp.append([0,(3**0.5)/3*ln, 1/3*ln])
        temp.append([ln/2,-(3**0.5)/6*ln,1/3*ln])
        temp.append([-ln/2,-(3**0.5)/6*ln,1/3*ln])

        self.vertices = np.array(temp)
        self.vertices += self.center
        self.orignal_vertices = self.vertices.copy()

    def tick(self) -> None:

        self.radian += 0.1

        self.vertices = trans.rotateZ(self.orignal_vertices, self.radian, self.center)

        if int(self.radian + 1) % 2 == 0:
            self.payload.append(self.vertices)
        pass        