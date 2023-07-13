from src.scenes import External
from src import transformations as trans
from shutil import get_terminal_size

class Torus(External):
    def __init__(self) -> None:
        super().__init__('torus', 20)
        self.radian = 0

    def tick(self) -> None:
        self.radian += 0.1

        self.vertices = trans.rotateY(
        trans.rotateX(trans.rotateZ(self.original_vertices, self.radian, self.center),self.radian,self.center), 
        self.radian, 
        self.center
        )