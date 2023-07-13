# Credit: https://blender.stackexchange.com/questions/69881/vertices-coords-and-edges-exporting

import bpy
import pathlib

obdata = bpy.context.object.data

name = "torusMIN"

path = pathlib.Path.home() / "Downloads" / "blenderExport" / f"{name}.csv"

fp = open(path, mode='w')

for v in obdata.vertices:
    x,y,z = v.co
    print(f'vertex,{v.index},{x:.2f},{y:.2f},{z:.2f}', file=fp)

for e in obdata.edges:
    v = e.vertices
    print(f'edge,{v[0]},{v[1]}', file=fp)
    
fp.close()