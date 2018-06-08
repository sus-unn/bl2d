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


from . import bl2d
from . import key_export
from . import preview_full
from . import sheet
from . import correction
    
import os
import bpy

import bpy.utils.previews
from bpy.types import Menu, Panel, UIList

class View3DPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'


class VIEW3D_PT_tools_bl2d_info(View3DPanel, Panel):

    bl_category = "BL2D"
    bl_label = "BL2D"
    bl_context = "objectmode"
    
    def draw(self, context):
        global bl2d_icons
        
        layout = self.layout
        
        col = layout.column()
        # col.label(text = "BL2D", icon_value = bl2d_icons["custom_icon"].icon_id)
        box = layout.box()
        box.label("Info")
        box.label("Version 0.6.7")
        col=layout.column()
        
        
class VIEW3D_PT_tools_bl2d_output(View3DPanel, Panel):

    bl_category = "BL2D"
    bl_label = "Output"
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        
        col = layout.column()        
        
        layout.operator("export.keys", text = "Export keyframes")
        layout.operator("export.preview_full", text = "Export full sheet preview")

class VIEW3D_PT_tools_bl2d_sheet(View3DPanel, Panel):

    bl_category = "BL2D"
    bl_label = "Sheet"
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        
        col = layout.column()
        col.label(text = "Move sheet origin point")
        col = layout.column()
        row = col.row()
        
        row.operator("object.sheet_op_mv_ul", text = "Upper Left")
        row.operator("object.sheet_op_mv_ur", text = "Upper Right")
        
        col = layout.column(align = True)
        row = col.row()

        row.operator("object.sheet_op_mv_ll", text = "Lower Left")
        row.operator("object.sheet_op_mv_lr", text = "Lower Right")
        
        col = layout.column() 
        col = layout.column() 
        
        col.label(text = "Correction paper")
        
        row = col.row()
        
        row.operator("gpencil.correctionadd", text = "Add correction paper")
        row.operator("gpencil.correctionrm", text = "Remove correction paper")
        
        col = layout.column(align = True)
        
        col.operator("gpencil.correctionchcol", text = "Change correction color")
        col.operator("gpencil.correctionresz", text = "Resize correction paper")
        
        col = layout.column() 
        col = layout.column()
        
class VIEW3D_PT_tools_bl2d_indicators(View3DPanel, Panel):

    bl_category = "BL2D"
    bl_label = "Indicators"
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()        
        
class VIEW3D_PT_tools_bl2d_book(View3DPanel, Panel):

    bl_category = "BL2D"
    bl_label = "Book"
    bl_context = "objectmode"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()   
