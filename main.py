from src.renderer import Renderer
from src.scenes import Cube
from src.scenes import line
from src.scenes import Tetrahedron
from src.scenes import External
from src.scenes import Torus

cu = Cube()
ln = line.Line()
tr = Tetrahedron()
ex = External('torus', scale=10)
to = Torus()
rd = Renderer(to)
rd.run()