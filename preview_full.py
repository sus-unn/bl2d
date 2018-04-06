import bpy
import os
from . import bl2d

inch_ratio = 1/25.399

dpi = 128

current_cam = bpy.context.scene.camera 
current_render_width = bpy.data.scenes['Main'].render.resolution_x 
current_render_height = bpy.data.scenes['Main'].render.resolution_y
fpath = bpy.data.scenes['Main'].render.filepath
fname = "Preview"


#Set Print Camera

bpy.context.scene.camera = bpy.data.objects['Camera_WholeSheet']
 
#Set Print Sheet

bpy.data.scenes['Main'].render.resolution_x = bpy.data.objects['Sheet'].scale[0] * dpi * inch_ratio * 100
bpy.data.scenes['Main'].render.resolution_y = bpy.data.objects['Sheet'].scale[1] * dpi * inch_ratio * 100




bpy.data.scenes['Main'].render.filepath = fpath + fname

bpy.ops.render.opengl(animation=True, sequencer=False, write_still=False, view_context=True)



#restore Camera
bpy.context.scene.camera = current_cam
#restore render settings
bpy.data.scenes['Main'].render.resolution_x = current_render_width
bpy.data.scenes['Main'].render.resolution_y = current_render_height 

bpy.data.scenes['Main'].render.filepath = fpath
bpy.context.scene.frame_set(bpy.data.scenes['Main'].frame_start)
