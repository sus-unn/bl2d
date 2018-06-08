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

# we need UI classes for:
# add correction paper
# remove correction paper
# change color
# resize

class CorrectionAdd(bpy.types.Operator):
    bl_idname  = "gpencil.correctionadd"
    bl_label = "Add correction paper"
    bl_descprtion = "Add correction paper to current frame"
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
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
