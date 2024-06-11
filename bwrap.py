from functools import wraps
from bops import bopen, bclose
import os 

def blender_executive(func):
    @wraps(func)
    def wrapper(
        subfolder: str = "subfolder", 
        filename: str = "filename",
        clear: bool = True,
        **kwargs
    ):
        blender_root = os.path.dirname(__file__)
        rootdir = os.path.join(blender_root, subfolder)
        if not os.path.exists(rootdir):
            os.makedirs(rootdir)
        name = filename
        mainfile_path = os.path.join(rootdir, name + ".blend")
        bopen(mainfile_path, clear=clear)
        # core func
        func(rootdir, **kwargs)
        # save and close
        bclose(mainfile_path)
    return wrapper