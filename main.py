from src.renderer import Renderer
from src.scenes import Cube, Line, Tetrahedron, External, Torus, MovingCube, SheerCube

Scenes = [Cube(), Line(), Tetrahedron(), Torus(), MovingCube(), SheerCube()]


for i, sc in enumerate(Scenes):
    print(f'{i+1}: {sc.__class__.__name__}')
idx = int(input("Choose which scene to render: ")) - 1


rd = Renderer(Scenes[idx], dump=True)
rd.run()