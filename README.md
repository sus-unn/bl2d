#sus_bl2d
#Utilities helps making 2d animation in blender

#PLEASE DONNOT TYPE ANY NON-ENGLISH CHARACTERS IN SCRIPTS including 'bl2d.py'
#DONNOT CHANGE ANY TEMPLATE OBJECT NAMES. IT WILL CAUSE FATAL ERROR.

#This add-on and its features are yet incomplete.
#================================================================================================

Basic Info:
	
	Animation Drawing In Blender
	
	Version 0.004.008d alpha
	
	Creator : Sus-susnn
	
	Contact me: typ3ys.xz@gmail.com, https://twitter.com/SusunnK  (DM available)
	
	Repository: https://github.com/sus-unn/bl2d
	
	
#Mirror: not ready yet..

	
	
Template Output:

#Preview(default)

	Frame Size = 1280 * 720
	
#Sheet (Printing) (default)

	DPI = 128
	
	Sheet Size = A4
	

Required:

    Add add-on zip file as Add-On(Install Add-On from file)
    
    Enable 'International fonts'
	Blender 
	Blender version must be at least 2.79
    
Recommanded: 

    BLAM (https://github.com/stuffmatic/blam)
    
    Layer Management (is in blender by default, yet disabled)
	
	for Developers:
		Git
		Python

	
#how to use:

	(0. This is alpha version and add-on is not ready yet. Adding add-on in user preference will do nothing. )
	
	1. install blender 2.79 or later versions. ("AT LEAST 2.79, template or script might not work in earlier versions")
	
	2. download from https://github.com/sus-unn/bl2d as zip file, or in terminal: "git clone https://github.com/sus-unn/bl2d.git"
	
	3. DONNOT DELETE ZIP FILE. If you've downloaded through git client, make copy of all files in one .zip file.
	
	4. In Blender User Preferences menu: install Add-on from zip file
	
	5. If you downloaded directly, unzip and open "template.blend".
	
	6. 'Save as' or copy template file in directory\name you want. You must not edit template file.
	
	
#incomplete features:
	
	1. 'Printing' script requires user to turn 3dView Panel to 'Camera view' mode.
	
	2. Time sheet is not ready.
	
	3. Automated layout text creation is not complete.
	
	4. It is not decided how to mark in-between for timesheet.
	
	5. Add-On file is practically blank.
	
	6. 'Preset_Lib' is incomplete.
	
	



Tips:

	Press 0 to view from (active) camera
	Press 0 again to go back to user view
	Press ctrl + 0 to make selected camera active
	Roll MMB to zoom in/out
	Press MMB and move mouse to rotate camera
	Press shift + MMB and move mouse to PAN camera
	Press shift + numpad 4 to rotate view left
	Press shift + numpad 6 to rotate view right
	Press ctrl+shift+MMB and move mouse to zoom more
	Press T to open/close toolbar (left side)
	Press N to open/close properties (right side)
	
	Press D to draw grease pencil
	Press D + RMB to erase grease pencil
	
	Press alt+a to preview animation
	
	to render with grease pencil, use OpenGL Render Animation.
	
	
	Moving 'Camera_2dPanTBTU' in X and Z axis will PAN camera. 
	Moving 'Camera_2dPanTBTU' in Y axis plus will TU camera.
	Moving Camera_2dPanTBTU' in Y axis minus will TB camera.
	'Camera_Main' will always aim to 'Camera_3DAimTarget'
	
	
	Scene "Main" is main working space.
	Scene "TimeSheet" is scene for time sheet(or, X-Sheet).
	Scene "Preset_Lib" is scene containing preset objects. (Like follow, 中割り indicators)
	
	Some objects are unselectable or hidden by default, because they might be distractive. 
	
	If you installed new version, and same UI panel is being repeated, or old version's panel is not being removed, press F8. 
	If that doesn't work, make an Issue on Github page or, mail me.
	
For Developers:

#Please contribute

	1. install git
	2. in terminal(Windows: Powershell or cmd), type: "git clone https://github.com/sus-unn/bl2d"
	3. if you don't know anything about git, please google 'git' and learn about it.
    4. Version => 'product number'.'feature  changes'.'minor changes'+TYPE:
        for exampe, 0.004.014b (product number zero, 4 feature changes, 14 minor changes, beta)
        a=alpha, b=beta, d=dev, u=unstable, r=release
    5. Tag version in git. (but don't tag every little commits)
