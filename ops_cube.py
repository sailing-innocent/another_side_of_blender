from bops import bopen, bclose, brender
import os 
mainfile_path = "sample.blend"
bopen(mainfile_path, clear=False)
brender(os.path.dirname(__file__), "target.png")
bclose(mainfile_path)
