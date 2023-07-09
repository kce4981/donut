import shutil
import sys
import time
import itertools

class Renderer:
    def __init__(self, scene):
        self.scene = scene
        self.seq = itertools.cycle(["@", "."])
    
    def tick(self):
        width, height = shutil.get_terminal_size()
        char = next(self.seq)

        for _ in range(height):
            print(char*width)
        sys.stdout.flush()
        
        # self.scene.tick()

    def run(self):
        while(True):
            self.tick()
            time.sleep(0.1)


if __name__ == '__main__':
    test = Renderer('test')
    test.run()
