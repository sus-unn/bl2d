# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
# Contributors:
# Sus-unn

import bpy
import os
from . import bl2d

class preview_full_export(bpy.types.Operator):

    bl_idname  = "export.preview_full"
    bl_label = "Export preview of full sheet"
    bl_descprtion = "Export preview of full sheet"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        
        bl2d.scene = bpy.data.scenes['Main']

        current_cam = bpy.context.scene.camera 
        current_render_width = bl2d.scene.render.resolution_x 
        current_render_height = bl2d.scene.render.resolution_y
        fpath = bl2d.scene.render.filepath
        fname = "Preview"


        #Set Print Camera

        bpy.context.scene.camera = bpy.data.objects['Camera_WholeSheet']
 
        #Set Print Sheet

        bl2d.scene.render.resolution_x = bpy.data.objects['Sheet'].scale[0] * bl2d.scan_dpi * bl2d.inch_ratio * 100
        bl2d.scene.render.resolution_y = bpy.data.objects['Sheet'].scale[1] * bl2d.scan_dpi * bl2d.inch_ratio * 100




        bl2d.scene.render.filepath = fpath + fname

        bpy.ops.render.opengl(animation=True, sequencer=False, write_still=False, view_context=True)



        #restore Camera
        bpy.context.scene.camera = current_cam
        #restore render settings
        bl2d.scene.render.resolution_x = current_render_width
        bl2d.scene.render.resolution_y = current_render_height 
        
        bl2d.scene.render.filepath = fpath
        bpy.context.scene.frame_set(bl2d.scene.frame_start)
        
        return {'FINISHED'}