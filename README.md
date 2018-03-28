#sus_bl2d
#Utilities helps making 2d animation in blender

#PLEASE DONNOT TYPE ANY NON-ENGLISH CHARACTERS IN 'bl2d.py'
#DONNOT CHANGE ANY TEMPLATE OBJECT NAMES. IT WILL CAUSE FATAL ERROR.

#This add-on and its features are yet incomplete.
#================================================================================================

Basic Info:
	
	Anime Drawing In Blender
	
	Version 0.01
	
	Creator : Sus-susnn
	
	Contact me: typ3ys.xz@gmail.com, https://twitter.com/SusunnK  (DM available)
	
	Repository: https://github.com/sus-unn/sus_bl2d
	
	
#Mirror: not ready yet..

	
	
Template Output:

#Preview(default)

	Frame Size = 1280 * 720
	
#Sheet (Printing) (default)

	DPI = 128
	
	Sheet Size = A4
	

Required:

    Add 'bl2d.py' as Add-On(Install Add-On from file)
    
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

	1. install blender 2.79 or later versions. ("AT LEAST 2.79, template or script might not work in earlier versions")
	
	2. download from https://github.com/sus-unn/sus_bl2d as zip file, or in terminal: "git clone https://github.com/sus-unn/sus_bl2d"
	
	3. DONNOT UNZIP ZIP FILE. If you've downloaded through git directly, zip all files in one .zip file.
	
	4. In Blender User Preferences menu: install Add-on from zip file
	
	5. Open "Template_A4.blend"
	
	6. 'Save as' or copy template file in directory\name you want. You must not edit template file.
	



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
	
For Developers:

#Please contribute

	1. install git
	2. in terminal(Windows: Powershell or cmd), type: "git clone https://github.com/sus-unn/sus_bl2d"
	3. when changes are made and saved, or if you want to add a file: "git add file_you_want_to_add"
	
#if file is in different directory, you will have to type directory of the file as well

	4. if new to git, or just-installed-git: in terminal, type: "git config --global user.email "your_email_adresss""
	5. to actually commit changes, in terminal, type: "git commit -m "Changes_you've_made""
	6. if you want to apply changes to the main branch my repository, type: "git push origin master"
	7. you might make branches of your own, type: git checkout -b "BRANCH_NAME". And pushing changes into your branch, not master, is much more safer. 

#for ones who don't know, you must press return key(Enter) to run command in terminal.
