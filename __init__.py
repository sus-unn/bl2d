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
    'version': (0, 6, 7),
    'blender': (2, 79, 0),
    'location': 'Toolshelf > BL2D',
    'description': 'Make 2D animation in blender. This add-on and template file is yet uncomplete.',
    'tracker_url': 'https://github.com/sus-unn/bl2d/issues',
    'warning': 'Features are unstable and under early stage of developement',
    'wiki_url': 'https://github.com/sus-unn/bl2d',
    'support': 'COMMUNITY',
    'category': 'Animation'}
    
if "bpy" in locals():
    import importlib
    importlib.reload(bl2d)
    importlib.reload(key_export)
    importlib.reload(preview_full)
    importlib.reload(sheet)
    importlib.reload(ui)
    
else:
    from . import bl2d
    from . import key_export
    from . import preview_full
    from . import sheet
    from . import ui
    
import os
import bpy


'''    
class SetTimeText(bpy.types.Operator):

    bl_label = "SetTimeText"
    bl_idname = "object.settimetext"
    def execute(self, context):
        bpy.data.objects["Text_Time_Second"].data.body = str(bpy.data.scenes["Main"].frame_end//bpy.data.scenes['Main'].render.fps)
        bpy.data.objects["Text_Time_Frame"].data.body = str(bpy.data.scenes["Main"].frame_end%bpy.data.scenes['Main'].render.fps)
        return {'RUNNING_MODAL'}

'''
# bl2d_icons = None

    
def register():
    # global bl2d_icons
    # bl2d_icons = bpy.utils.previews.new()
    # script_file = os.path.realpath(__file__)
    # bl2d_icons.load("custom_icon", os.path.join(os.path.dirname(script_file),"icons","bl2d_ico.png"), 'IMAGE')
    bpy.utils.register_module(__name__)
    
    
def unregister():
    global custom_icons
    # bpy.utils.previews.remove(bl2d_icons)
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()

