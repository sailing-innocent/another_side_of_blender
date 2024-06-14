from bwrap import blender_executive
from bops import brender 
from bobj import simple_cube
# import sys 
# import os 
# sys.path.append(
#     os.path.join(
#         os.path.dirname(__file__), 
#         "BlenderPythonRenderer"
#     ))
import bpy 

@blender_executive
def change_engine(rootdir):
    simple_cube()
    # bpy.utils.register_class(CustomRenderEngine)
    # enable
    scene = bpy.context.scene 
    scene.render.engine = 'CYCLES'
    # scene.render.engine = 'BPR'
    brender(rootdir, 'change_engine.png')
    # bpy.utils.unregister_class(CustomRenderEngine)

if __name__ == "__main__":
    change_engine(subfolder="demo", filename="change_engine")
