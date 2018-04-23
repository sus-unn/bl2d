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

from . import bl2d

class SheetOriginMoveLU(bpy.types.Operator):
    
    bl_idname = "object.sheet_op_mv_lu"
    bl_label = "Move sheet origin point"
    bl_description = "Move sheet origin point to upper left vertex, so that we can extend them in certain direction."
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}
        
class SheetOriginMoveLL(bpy.types.Operator):
    
    bl_idname = "object.sheet_op_mv_ll"
    bl_label = "Move sheet origin point"
    bl_description = "Move sheet origin point to lower left vertex, so that we can extend them in certain direction."
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}
        
class SheetOriginMoveRU(bpy.types.Operator):
    
    bl_idname = "object.sheet_op_mv_ru"
    bl_label = "Move sheet origin point"
    bl_description = "Move sheet origin point to upper right vertex, so that we can extend them in certain direction."
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}
        
class SheetOriginMoveRL(bpy.types.Operator):
    
    bl_idname = "object.sheet_op_mv_rl"
    bl_label = "Move sheet origin point"
    bl_description = "Move sheet origin point to lower right vertex, so that we can extend them in certain direction."
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}
        
