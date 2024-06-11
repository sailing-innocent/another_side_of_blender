import bpy
import os 

mainfile_path = "sample.blend"
filepath = os.path.join(os.path.dirname(__file__), "target.png")
# 如果没找到sample.blend，就保存一个新的
if (not os.path.exists(mainfile_path)):
    bpy.ops.wm.save_mainfile(filepath=mainfile_path)
# 打开sample.blend文件
bpy.ops.wm.open_mainfile(filepath = mainfile_path)
# 拿到当前的场景
scene = bpy.context.scene 
# 设定渲染的目标地址
scene.render.filepath = filepath
# 渲染
bpy.ops.render.render(write_still=True)
# 保存文件，相当于 ctrl + s
bpy.ops.wm.save_mainfile(filepath=mainfile_path)