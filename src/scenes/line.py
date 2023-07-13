import numpy as np

from src import transformations as trans
from src.scenes import Base


class Line(Base):
    def __init__(self):
        super().__init__()
        self.count = 0
        
        self.edges = [(0,1)]
        temp = []
        temp.append([20, 10, 20])
        temp.append([30, 10, 40])

        self.original_vertices = np.array(temp)
        self.vertices = np.array(temp)

        self.center = np.array([25, 10, 30])

    def tick(self):

        self.vertices = trans.rotateX(self.original_vertices, self.count, self.center)

        self.count += 0.1

