import bpy 
import numpy as np 

# Scene
# DummyRenderer
class DummyEngine(bpy.types.RenderEngine):
    bl_idname = "DUMMY_ENGINE"
    bl_label = "Dummy Engine"
    bl_use_preview = False 

    def __init__(self):
        self.scene_data = None 
        self.draw_data = None 
        # self.renderer = DummyRenderer()
    
    def __del__(self):
        pass 

    def render(self, depsgraph):
        bscene = depsgraph.scene 
        # bind scene according to bscene
        scale = bscene.render.resolution_percentage / 100.0
        size_x = int(bscene.render.resolution_x * scale)
        size_y = int(bscene.render.resolution_y * scale)
        # self.renderer.set_size(size_x, size_y)
        # build camera info based on size
        # pixels = renderer.render(scene, camera)
        pixels = np.ones((size_x, size_y, 4), dtype=np.float32)
        # set pixels to cyan
        pixels[:, :, 0] = 0.0 
        rect = [pixels[i, j, :].tolist() for i in range(size_x) for j in range(size_y)]
        # Here we write the pixel values to the RenderResult
        result = self.begin_result(0, 0, size_x, size_y)
        layer = result.layers[0].passes["Combined"]
        layer.rect = rect
        self.end_result(result)

    def view_update(self, context, depsgraph):
        pass 
    def view_draw(self, context, depsgraph):
        pass 