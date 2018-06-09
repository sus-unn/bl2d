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
import copy

from . import bl2d

# we need UI classes for:
# add correction paper
# remove correction paper
# change color
# resize

def fCorrectionAdd(color):
    print("\nAdd correction paper") # debug
        
    if not bpy.context.scene.grease_pencil.layers.active.frames:
        bpy.ops.gpencil.blank_frame_add()
    str = bpy.context.scene.grease_pencil.layers.active.active_frame.strokes.new(colorname=color)
    str.draw_mode = '3DSPACE'
    str.line_width = 1
    str.points.add(count=4)
    
    # copy world coordinate of each vertices in Sheet_Base to v
    # for loop in v
    
    v = [[[0],[0],[0]], [[0],[0],[0]], [[0],[0],[0]], [[0],[0],[0]]]
    # globa_coord = bpy.data.objects['Sheet_Base']matrix_world * bpy.data.objects['Sheet_Base'].data.vertices[0].co[0]
    
    # copy coordinates
    # Sheet_Base vertices id goes like 0,1,3,2.. so it has to be like this. Without using loop.
    v[0] = copy.copy(bpy.data.objects['Sheet_Base'].data.vertices[0].co) 
    v[1] = copy.copy(bpy.data.objects['Sheet_Base'].data.vertices[1].co) 
    v[2] = copy.copy(bpy.data.objects['Sheet_Base'].data.vertices[3].co) 
    v[3] = bpy.data.objects['Sheet_Base'].matrix_world.to_translation()
    print("\nlocal coordinates:")
    print(v)
        
    # get global coordinates
    for i in range (0,3):
        v[i] = bpy.data.objects['Sheet_Base'].matrix_world * v[i]
    print("\nInitial copy:")
    print(v)
      
    # v[3] = loc = bpy.data.objects['Sheet_Base'].matrix_world.to_translation()
    for l in range(0,3):
        str.points[l].co = copy.copy(tuple(v[l]))
        
    str.points[3].co[0] = v[3][0]
    str.points[3].co[1] = v[3][1]
    str.points[3].co[2] = v[3][2]
    print("\ncreated strokes: ") # debug
    for i in range(0,4): 
        print(i, " : ", str.points[i].co) 
    print('\n')
    # done
        

class CorrectionAddYellow(bpy.types.Operator):
    bl_idname  = "gpencil.correctionaddyellow"
    bl_label = "Add correction paper"
    bl_descprtion = "Add correction paper to current frame"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        fCorrectionAdd('CorrectionYellow')
        return {'FINISHED'}

class CorrectionAddBlue(bpy.types.Operator):
    bl_idname  = "gpencil.correctionaddblue"
    bl_label = "Add correction paper"
    bl_descprtion = "Add correction paper to current frame"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        fCorrectionAdd('CorrectionBlue')
        return {'FINISHED'}
        
class CorrectionAddGreen(bpy.types.Operator):
    bl_idname  = "gpencil.correctionaddgreen"
    bl_label = "Add correction paper"
    bl_descprtion = "Add correction paper to current frame"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        fCorrectionAdd('CorrectionGreen')
        return {'FINISHED'}
        
class CorrectionAddPink(bpy.types.Operator):
    bl_idname  = "gpencil.correctionaddpink"
    bl_label = "Add correction paper"
    bl_descprtion = "Add correction paper to current frame"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        fCorrectionAdd('CorrectionPink')
        return {'FINISHED'}

class CorrectionRemove(bpy.types.Operator):
    bl_idname  = "gpencil.correctionrm"
    bl_label = "Remove correction paper"
    bl_descprtion = "Remove correction paper from current frame"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}

class CorrectionChangeColor(bpy.types.Operator):
    bl_idname  = "gpencil.correctionchcol"
    bl_label = "Remove color of correction paper"
    bl_descprtion = "Remove color of correction paper of current frame"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}

class CorrectionResize(bpy.types.Operator):
    bl_idname  = "gpencil.correctionresz"
    bl_label = "Resize correction paper"
    bl_descprtion = "Resize current cel's correction paper"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}
