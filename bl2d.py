
import os
import bpy
import bpy.utils.previews


bl_info = { \
    'name': 'BL2D: Blender 2D Animation toolkit for digital hand-drawn animation (Alpha)',
    'author': 'Susunn',
    'version': (0, 1, 2),
    'blender': (2, 7, 9),
    'location': 'Toolshelf > Tools',
    'description': 'Make 2D animation in blender. This add-on and template file is yet uncomplete.',
    'tracker_url': 'https://github.com/sus-unn/bl2d',
    'wiki_url': 'https://github.com/sus-unn/bl2d',
    'support': 'COMMUNITY',
    'category': 'Animation'}
	


class BL2dPanel(bpy.types.Panel):
	'''
	bl2d panel class
	'''
	
	bl_label = "BL2D"
	bl_idname = "OBJECT_PT+BL2D"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_context = "objectmode"
	
	def draw(self, context):
		global bl2d_icons
		
		layout = self.layout
		
		row = layout.row()
		row.label(text = "BL2D", icon_value = bl2d_icons["custom_icon"].icon_id)
		
		box = layout.box()
		box.label("Info")
		
		row=box.row()
		
		row=layout.row()
		box=layout.box()
		box.label("Print")
		
		row=box.row()
		
		row=layout.row()
		box=layout.box()
		box.label("Indicators")
		
		row=box.row()
	
	

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

