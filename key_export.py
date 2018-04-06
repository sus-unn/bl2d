import bpy
import os
from . import bl2d

inch_ratio = 1/25.399

key_jump_next = 0
key_jump_prev = 1


def key_export(gp_layer_name):

    bl2d.scene.frame_set(bl2d.scene.frame_start-1)
            
    key_count_blend = 0
    key_count_sheet = 1
            
    while True:
        if bpy.ops.screen.keyframe_jump(key_jump_next) == {'CANCELLED'}:
            break
                
        key_count_str = str(key_count_sheet)
                
        if (key_count_sheet < 0) or (key_count_sheet > 9999):
            print("Error in key_export: too much keyframes. Maximum count of each cel's keyframe is 9999.")
            
        if(key_count_sheet < 10):
            key_count_str = "000" + key_count_str
        if(10 <= key_count_sheet < 100):
            key_count_str = "00" + key_count_str
        if(100 <= key_count_sheet < 1000):
            key_count_str = "0" + key_count_str
        bl2d.scene.render.filepath = bl2d.fpath + bl2d.fname + "_" + gp_layer_name + "_"
        bl2d.scene.render.filepath += str(key_count_str)
        if bl2d.gp_layers[gp_layer_name].frames[key_count_blend].strokes.items():
            bpy.ops.render.opengl(animation=False, sequencer=False, write_still=True, view_context=True)
            key_count_sheet += 1
        key_count_blend += 1

class ExportKey(bpy.types.Operator):
    
    bl_idname = "export.keys"
    bl_label = "Export keyframes"
    bl_description = "Export keyframe sheets at once. "
    
    @classmethod
    def poll(cls, context):
        return context.object is not None
        
    def execute(self, context):
        #currently this variables are pre-defined

        dpi = 300
        
        bl2d.scene = bpy.data.scenes['Main']
        bl2d.gp_layers = bpy.data.grease_pencil['GPencil_Main'].layers
        
        #backups
        current_format = bl2d.scene.render.image_settings.file_format
        current_cam = bpy.data.objects['Camera_Main']
        #current_cam = bl2d.scene.camera #this one is alternative
        current_render_width = bl2d.scene.render.resolution_x 
        current_render_height = bl2d.scene.render.resolution_y
        
        current_color_mode = bl2d.scene.render.image_settings.color_mode
        current_color_depth = bl2d.scene.render.image_settings.color_depth
        current_compression = bl2d.scene.render.image_settings.compression
        
        #export settings
        bl2d.scene.render.image_settings.file_format = 'PNG'
        bl2d.fpath = bl2d.scene.render.filepath 
        xpath = bl2d.fpath #export directory
        
        bl2d.scene.render.image_settings.color_mode = 'RGB'
        bl2d.scene.render.image_settings.color_depth = '8'
        bl2d.scene.render.image_settings.compression = 15
        
        
        #Set Print Camera
        
        bl2d.scene.camera = bpy.data.objects['Camera_WholeSheet']
        
        #Set Print Sheet
        
        bl2d.scene.render.resolution_x = bpy.data.objects['Sheet'].scale[0] * dpi * inch_ratio * 100
        bl2d.scene.render.resolution_y = bpy.data.objects['Sheet'].scale[1] * dpi * inch_ratio * 100
        
        bl2d.scene.frame_set(bl2d.scene.frame_start)
        
        #print all cels here
        
        for each_gp_layer in bl2d.gp_layers: #hide all layers
            each_gp_layer.hide = True
        
        for each_gp_layer in bl2d.gp_layers:#print each layers
            each_gp_layer.hide = False #unhide current layer and...
            key_export(each_gp_layer.info)
            each_gp_layer.hide = True #...hide current layer again.
        
        for each_gp_layer in bl2d.gp_layers: #unhide all GPencil Layers
            each_gp_layer.hide = False
        
        
        
        #restore Camera
        bl2d.scene.camera = current_cam
        #restore render settings
        bl2d.scene.render.image_settings.file_format = current_format
        bl2d.scene.render.resolution_x = current_render_width
        bl2d.scene.render.resolution_y = current_render_height 
        
        bl2d.scene.render.image_settings.color_mode = current_color_mode
        bl2d.scene.render.image_settings.color_depth = current_color_depth
        bl2d.scene.render.image_settings.compression = current_compression
        
        bl2d.scene.render.filepath = bl2d.fpath
        bl2d.scene.frame_set(bl2d.scene.frame_start)
        return {'FINISHED'}

 