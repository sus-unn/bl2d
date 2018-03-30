import bpy
import os

context_format = bpy.data.scenes['Main'].render.image_settings.file_format
bpy.data.scenes['Main'].render.image_settings.file_format = 'PNG'

key_jump_next = 0
key_jump_prev = 1

inch_ratio = 1/25.399

dpi = 300

current_cam = bpy.data.objects['Camera_Main']
#current_cam = bpy.context.scene.camera #this one is alternative
current_render_width = bpy.data.scenes['Main'].render.resolution_x 
current_render_height = bpy.data.scenes['Main'].render.resolution_y
fpath = bpy.data.scenes['Main'].render.filepath
fname = "image"

#Set Print Camera

bpy.context.scene.camera = bpy.data.objects['Camera_WholeSheet']
 
#Set Print Sheet

bpy.data.scenes['Main'].render.resolution_x = bpy.data.objects['Sheet'].scale[0] * dpi * inch_ratio * 100
bpy.data.scenes['Main'].render.resolution_y = bpy.data.objects['Sheet'].scale[1] * dpi * inch_ratio * 100

def key_export(gp_layer_name):
    bpy.context.scene.frame_set(bpy.data.scenes['Main'].frame_start-1)
    
    key_count_blend = 0
    key_count_sheet = 1
    
    while True:
        if bpy.ops.screen.keyframe_jump(key_jump_next) == {'CANCELLED'}:
            break
        bpy.data.scenes['Main'].render.filepath = fpath + fname + "_" + gp_layer_name + "_"
        bpy.data.scenes['Main'].render.filepath += str(key_count_sheet)
        if bpy.data.grease_pencil['GPencil_Main'].layers[gp_layer_name].frames[key_count_blend].strokes.items():
            bpy.ops.render.opengl(animation=False, sequencer=False, write_still=True, view_context=True)
            key_count_sheet += 1
        key_count_blend += 1
        
        

bpy.context.scene.frame_set(bpy.data.scenes['Main'].frame_start)

#print all cels here

for each_gp_layer in bpy.data.grease_pencil['GPencil_Main'].layers: #hide all layers
    each_gp_layer.hide = True

for each_gp_layer in bpy.data.grease_pencil['GPencil_Main'].layers:#print each layers
    each_gp_layer.hide = False #unhide current layer and...
    key_export(each_gp_layer.info)
    each_gp_layer.hide = True #...hide current layer again.

for each_gp_layer in bpy.data.grease_pencil['GPencil_Main'].layers: #unhide all GPencil Layers
    each_gp_layer.hide = False



#restore Camera
bpy.context.scene.camera = current_cam
#restore render settings
bpy.data.scenes['Main'].render.image_settings.file_format = context_format
bpy.data.scenes['Main'].render.resolution_x = current_render_width
bpy.data.scenes['Main'].render.resolution_y = current_render_height 

bpy.data.scenes['Main'].render.filepath = fpath
bpy.context.scene.frame_set(bpy.data.scenes['Main'].frame_start)
