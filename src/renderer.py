import shutil
import sys
import time
import itertools
import numpy as np
from src.scenes import Base

class Renderer:
    def __init__(self, scene: Base, dump=False):
        self.scene = scene
        self.seq = itertools.cycle(["@", "."])
        self.payload = []
        self.dump = dump
        self.count = 0


        self.scene.dump = self.dump
    
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


        if self.dump == False:
            return
        if self.count % 5 == 0:
            self.payload.append([self.scene.vertices.copy(), transformed_vertices.T.copy()])
        self.count += 1

    def render(self, width, height, vertices):

        self.screen = [[" " for _ in range(width)] for _ in range(height)]
        coord = []


        for ver in vertices:
            try:
                w = round(ver[0])
                h = round(ver[2])
            except OverflowError:
                continue
            except ValueError:
                continue

            coord.append((w,h))

        for idx in range(len(coord)):

            print(idx)

            for edge in self.scene.edges:
                if edge[0] != idx:
                    continue
                
                ver = coord[idx]
                ver_target = coord[edge[1]]

                print(ver)
                print(ver_target)

                pos_x = ver[0]
                pos_z = ver[1]

                # z / x
                delta_x = ver_target[0] - ver[0]
                delta_z = ver_target[1] - ver[1]
                distance = round((delta_x**2 + delta_z**2)**0.5)

                unit = 1 if delta_x >= 0 else -1
                

                print(delta_x, delta_z, distance)

                try:
                    slope = delta_z / delta_x
                except ZeroDivisionError:
                    # horizontal line
                    slope = False

                print(slope)

                if slope is False:
                    for _ in range(distance):
                        pos_z += unit
                        self.draw(pos_x, pos_z, height, width)

                    continue
                
                for _ in range(distance):
                    pos_x += unit
                    pos_z += unit * slope

                    self.draw(pos_x, pos_z, width, height)
        
        for ver in coord:
            self.draw(*ver, width, height)

        for s in self.screen:
            print(''.join(s))

        sys.stdout.flush()

    def draw(self, w, h, width, height):

        w = round(w)
        h = round(h)

        if w < 0 or w >= width:
            return
        if h < 0 or h >= height:
            return

        self.screen[h][w] = "@"

    def run(self):
        while(True):
            try:
                self.tick()
                time.sleep(0.1)
            except KeyboardInterrupt:
                self.scene.quit()

                if not self.dump:
                    break
                
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
