import numpy as np

class Cube:
    def __init__(self):
        temp = []
        temp.append([10, 10, 10])
        temp.append([30, 10, 10])
        temp.append([10, 10, 30])
        temp.append([30, 10, 30])
        self.vertices = np.array(temp)
