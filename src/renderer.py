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
        self.width = width
        self.height = height

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

            for edge in self.scene.edges:
                if edge[0] != idx:
                    continue
                
                ver = coord[idx]
                ver_target = coord[edge[1]]

                self.draw_line(*ver, *ver_target)
        
        for ver in coord:
            self.draw_Pixel(*ver)

        for s in self.screen:
            print(''.join(s))

        sys.stdout.flush()

    def draw_line(self, x1, z1, x2, z2):

        if abs(x2 - x1) > abs(z2 - z1):
            if x1 > x2:
                self.draw_line_x(x2, z2, x1, z1)
            else:
                self.draw_line_x(x1, z1, x2, z2)
        else:
            if z1 > z2:
                self.draw_line_z(x2, z2, x1, z1)
            else:
                self.draw_line_z(x1, z1, x2, z2)

        

    def draw_line_x(self, x1, z1, x2, z2):

        dx = x2 - x1
        dz = z2 - z1
        slope = dz / dx

        z = z1
        z_direction = 1
        if dz < 0:
            z_direction = -1
            slope *= -1
        D = 0.5

        for x in range(x1, x2+1):

            D += slope
            print(D)
            if D >= 1:
                D -= 1
                z += z_direction

            self.draw_Pixel(x, z)

    def draw_line_z(self, x1, z1, x2, z2):
        dx = x2 - x1
        dz = z2 - z1
        slope = dx / dz

        x = x1
        x_direction = 1
        if dx < 0:
            x_direction = -1
            slope *= -1
        D = 0.5

        for z in range(z1, z2+1):

            D += slope
            if D >= 1:
                D -= 1
                x += x_direction

            self.draw_Pixel(x, z)

    def draw_Pixel(self, w: int, h: int):

        if w < 0 or w >= self.width:
            return
        if h < 0 or h >= self.height:
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
