import pathlib
import csv
import numpy as np
from src.scenes import Base

class External(Base):
    def __init__(self, model: str, scale=1) -> None:
        super().__init__()
        self.edges = []
        self.scale = scale

        path = pathlib.Path(__file__).parents[2] / "models" / f'{model}.csv'

        with open(path, newline='') as fp:
            line = csv.reader(fp)
            self.process(line)


    def process(self, csv_list: list):
        vertex_temp = []
        for line in csv_list:
            if line[0] == 'origin':
                self.center = np.array(list(map(int, line[1:])))
            
            if line[0] == 'vertex':
                idx = int(line[1])
                coord = list(map(float, line[2:]))
                vertex_temp.append((idx, coord))

            if line[0] == 'edge':
                self.edges.append((int(line[1]), int(line[2])))
        
        vertex_temp.sort(key=lambda x: x[0])
        vertex = [ver[1] for ver in vertex_temp]
        self.vertices = np.array(vertex)*self.scale + self.center
        self.original_vertices = self.vertices.copy()

if __name__ == '__main__':
    external = External("export")


