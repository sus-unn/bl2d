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

v_UL = 0
v_LL = 1
v_UR = 2
v_LR = 3

def GetVertexPos(pos):
# backupt context (object, mode)
# get current mode
# if edit mode
#   goto object mode
# select sheet object
# check if count of verticeis ar not 4
# for each vertices, get ther coord
# compare them
# return vertex corresponds to arg
    return 0

class SheetOriginMoveUL(bpy.types.Operator):
    # the reason these SheetOriginMove classes not inheriting common parent class, but being code duplicated,
    # is that inheriting parent class which inehrits bpy.types.Operator 
    # makes these classes unregistered as an operator
    # so I had to just copy and paste codes
    # if anyone knows how to fix this issue, and fix it, I'll be thankful
    
    bl_idname = "object.sheet_op_mv_ul"
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
        
class SheetOriginMoveUR(bpy.types.Operator):
    
    bl_idname = "object.sheet_op_mv_ur"
    bl_label = "Move sheet origin point"
    bl_description = "Move sheet origin point to upper right vertex, so that we can extend them in certain direction."
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}
        
class SheetOriginMoveLR(bpy.types.Operator):
    
    bl_idname = "object.sheet_op_mv_lr"
    bl_label = "Move sheet origin point"
    bl_description = "Move sheet origin point to lower right vertex, so that we can extend them in certain direction."
    
    @classmethod
    def poll(cls, context):
        return bl2d.poll()
        
    def execute(self, context):
        return {'FINISHED'}
        
