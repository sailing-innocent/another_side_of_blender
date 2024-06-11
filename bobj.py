import bpy 
import mathutils 

def add_cube():
    # create object
    bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
    obj = bpy.context.object
    return obj

def track_to_constraints(obj, target):
    constraint = obj.constraints.new('TRACK_TO')
    constraint.target = target 
    constraint.track_axis = 'TRACK_NEGATIVE_Z'
    constraint.up_axis = 'UP_Y'

def create_basic_light(origin, type='POINT', energy=1000, color=(1,1,1), target=None):
    # Light types: 'POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'
    bpy.ops.object.add(type='LIGHT', location=origin)
    obj = bpy.context.object
    obj.data.type = type
    obj.data.energy = energy
    obj.data.color = color
    if target: 
        track_to_constraints(obj, target)
    return obj

def create_basic_camera(origin, target=None, camera_type='PERSP', lens=25, clip_start=0.1, clip_end=100, ortho_scale=6):
    # Create object and camera
    camera = bpy.data.cameras.new("Camera")
    camera.lens = lens 
    camera.clip_start = clip_start 
    camera.clip_end = clip_end 
    camera.type = camera_type # 'PERSP', 'ORTHO', 'PANO'
    if (camera_type == 'ORTHO'):
        camera.ortho_scale = ortho_scale

    # Link Object to Scene 
    obj = bpy.data.objects.new("CameraObj", camera)
    obj.location = origin 
    bpy.context.collection.objects.link(obj)
    bpy.context.scene.camera = obj # Make Current
    
    if target: 
        track_to_constraints(obj, target)

    return obj 

def simple_cube():
    obj = add_cube()
    camera = create_basic_camera(origin=mathutils.Vector((2, 6, 6)), target=obj)
    light  = create_basic_light(origin=mathutils.Vector((0, 5, 5)), target=obj)
    return obj, camera, light

