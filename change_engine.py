from bwrap import blender_executive
from bops import brender 
from bobj import simple_cube
from dummy_engine import DummyEngine
import bpy 

@blender_executive
def dummy_render(rootdir):
    simple_cube()
    bpy.utils.register_class(DummyEngine)
    scene = bpy.context.scene 
    # scene.render.engine = 'CYCLES'
    scene.render.engine = 'DUMMY_ENGINE'
    brender(rootdir, 'dummy_engine.png')

if __name__ == "__main__":
    dummy_render(subfolder="demo", filename="dummy_engine")