
from bwrap import blender_executive
from bops import brender 

@blender_executive
def dummy_render(rootdir):
    brender(rootdir, 'dummy_render.png')

if __name__ == "__main__":
    dummy_render(subfolder="demo", filename="dummy_render", clear=False)
