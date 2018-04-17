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

bl_info = { \
    'name': 'BL2D: Blender 2D Animation toolkit for digital hand-drawn animation (alpha)',
    'author': 'Susunn',
    'version': (0, 6, 6),
    'blender': (2, 79, 0),
    'location': 'Toolshelf > Tools',
    'description': 'Make 2D animation in blender. This add-on and template file is yet uncomplete.',
    'tracker_url': 'https://github.com/sus-unn/bl2d/issues',
    'wiki_url': 'https://github.com/sus-unn/bl2d',
    'support': 'COMMUNITY',
    'category': 'Animation'}
    
if "bpy" in locals():
    import importlib
    importlib.reload(bl2d)
    importlib.reload(key_export)
    importlib.reload(preview_full)
    
else:
    from . import bl2d
    from . import key_export
    from . import preview_full
    
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
        col.label(text = "BL2D", icon_value = bl2d_icons["custom_icon"].icon_id)
        
        box = layout.box()
        box.label("Info")
        
        box.label("Version 0.006.000d")
        box.label("ui_dev branch")
        
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

'''    
class SetTimeText(bpy.types.Operator):

    bl_label = "SetTimeText"
    bl_idname = "object.settimetext"
    def execute(self, context):
        bpy.data.objects["Text_Time_Second"].data.body = str(bpy.data.scenes["Main"].frame_end//bpy.data.scenes['Main'].render.fps)
        bpy.data.objects["Text_Time_Frame"].data.body = str(bpy.data.scenes["Main"].frame_end%bpy.data.scenes['Main'].render.fps)
        return {'RUNNING_MODAL'}

'''
bl2d_icons = None

    
def register():
    global bl2d_icons
    bl2d_icons = bpy.utils.previews.new()
    script_file = os.path.realpath(__file__)
    bl2d_icons.load("custom_icon", os.path.join(os.path.dirname(script_file),"icons","bl2d_ico.png"), 'IMAGE')
    bpy.utils.register_module(__name__)
    
    
def unregister():
    global custom_icons
    bpy.utils.previews.remove(bl2d_icons)
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()

