from bwrap import blender_executive
from bops import brender 
from bobj import simple_cube

@blender_executive
def manual_cube(rootdir):
    simple_cube()
    brender(rootdir, 'manual_cube.png')

if __name__ == "__main__":
    manual_cube(subfolder="demo", filename="manual_cube")
