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

def sheetlen(direction)

# ##########################
#       --------------
#       |                       |
# <-- |                       |
#       |                       |
#       --------------
# ##########################

class sheet_extend_left(bpy.types.Operator): 

    bl_idname  = "object.sheet_extned_left"
    bl_label = "Sheet_extend_left"
    bl_descprtion = "Extend current sheet 1cm to the left"
    
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
    
    
    
    
    
# ##########################
#       --------------
#       |                       |
#       |                       |  -->
#       |                       |
#       --------------
# ##########################
    
class sheet_extend_right(bpy.types.Operator):
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
        return {'FINISHED'}
        
        
        
        
    
# ##########################
#                   /\
#                   ||
#       --------------
#       |                       |
#       |                       | 
#       |                       |
#       --------------
# ##########################
    
class sheet_extend_up(bpy.types.Operator):
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
        return {'FINISHED'}
    
# ##########################
#       --------------
#       |                       |
#       |                       | 
#       |                       |
#       --------------
#                   ||
#                   \/
# ##########################




    
class sheet_extend_down(bpy.types.Operator):
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
        return {'FINISHED'}
        

        
# #################################################
# #################################################        
        
# ##########################
#       --------------
#       |                       |
# --> |                       |
#       |                       |
#       --------------
# ##########################

class sheet_shorten_left(bpy.types.Operator): 
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
        return {'FINISHED'}
    
    
    
    
# ##########################
#       --------------
#       |                       |
#       |                       |  <--
#       |                       |
#       --------------
# ##########################
    
class sheet_extend_right(bpy.types.Operator):
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
        return {'FINISHED'}
        
        
        
        
    
# ##########################
#                   ||
#                   \/
#       --------------
#       |                       |
#       |                       | 
#       |                       |
#       --------------
# ##########################
    
class sheet_extend_up(bpy.types.Operator):
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
        return {'FINISHED'}
        
        
        

    
# ##########################
#       --------------
#       |                       |
#       |                       | 
#       |                       |
#       --------------
#                   /\
#                   ||
# ##########################

class sheet_extend_down(bpy.types.Operator):
    @classmethod
    def poll(cls, context):
        return bpy.data.objects['Sheet_Base'] is not None
        
    def execute(self, context):
        return {'FINISHED'}