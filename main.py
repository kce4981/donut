from src.renderer import Renderer
from src.scenes import Cube

cu = Cube()
rd = Renderer(cu)
rd.run()