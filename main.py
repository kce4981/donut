from src.renderer import Renderer
from src.scenes import Cube
from src.scenes import line

cu = Cube()
ln = line.Line()
rd = Renderer(cu)
rd.run()