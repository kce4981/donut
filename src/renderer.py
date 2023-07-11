import shutil
import sys
import time
import itertools
import numpy as np
from src.scenes import Base

class Renderer:
    def __init__(self, scene: Base):
        self.scene = scene
        self.seq = itertools.cycle(["@", "."])
        self.payload = []
        self.count = 0
    
    def tick(self):
        width, height = shutil.get_terminal_size()

        camera_point = np.array((round(width/2), -20, round(height/2)))
        self.camera_point = camera_point
        vertex_vectors = self.scene.vertices - camera_point
        
        multiplier = []

        # zero division error will occur if a vertex has the same y pos as the camera_point has
        # needs to be fixed
        # value is inf if zeroDivision happens
        for x in range(np.shape(self.scene.vertices)[0]):
            n = self.scene.vertices[:,1][x] 
            d = vertex_vectors[:,1][x]
            # print(n, d)
            multiplier.append(n/d)

        # print(multiplier)

        multiplied_vertex_vectors = np.matmul(vertex_vectors.T, np.diag(np.array(multiplier)))
        transformed_vertices = self.scene.vertices.T - multiplied_vertex_vectors

        # i found a critical error while experimenting with different y values
        # this projection method projects the entire plane 
        # meaning not only the front, the back of the camera also will be projected
        # very good logic i have

        self.render(width, height, transformed_vertices.T)
        self.scene.tick()

        if self.count % 5 == 0:
            self.payload.append([self.scene.vertices.copy(), transformed_vertices.T.copy()])
        self.count += 1

    def render(self, width, height, vertices):

        screen = [[" " for _ in range(width)] for _ in range(height)]

        for ver in vertices:
            try:
                w = round(ver[0])
                h = round(ver[2])
            except OverflowError:
                continue

            if w < 0 or w >= width:
                continue
            if h < 0 or h >= height:
                continue

            screen[h][w] = "@"
        
        for s in screen:
            print(''.join(s))

        sys.stdout.flush()

    def run(self):
        while(True):
            try:
                self.tick()
                time.sleep(0.1)
            except KeyboardInterrupt:
                self.scene.quit()
                
                self.payload = [self.payload, self.camera_point]

                import pickle
                from pathlib import Path
                dump_path = Path(__file__).parents[1] / 'dumps' / 'Renderer.data'
                with open(dump_path, mode='wb') as fp:
                    pickle.dump(self.payload, fp)
                break


if __name__ == '__main__':
    from scenes import Cube
    cb = Cube()
    test = Renderer(cb)
    test.run()
