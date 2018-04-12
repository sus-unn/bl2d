BL2D Manual
===========

Installation(General)
----------------

1. In [official github repository](https://github.com/sus-unn/bl2d), press 'Clone or Download' and download as .zip file.

2. Add zip file as add-on in blender.

3. Unpack template.blend in zip file. (template.blend hereafter template)

4. Copy template to working directory, and change it's name into whatever you want.

5. You can draw layout and key animation in the template.

Installation(dev)
-------------

1. First of all, you must have git client in your desktop, and you must know how to use git.

2. In working directory, in terminal:
```bash
git clone --mirror https://github.com/sus-unn/bl2d.git bl2d/.git
cd bl2d
git config --unset core.bare
git config receive.denyCurrentBranch updateInstead
git checkout master
```
(By doing this, you will clone all the branches from the remote repository)

3. Including ".git" folder, pack the whole repo as zip file.

4. In blender, add .zip file as add-on.

5. Go to the user's add-on directory, find bl2d folder. Whole repository will be copied there!!

(In case of window, the user add-on is usually in %APPDATA%\Blender Foundation\Blender\(Belnder version)\scripts\addons\)

6. You can develope the add-on in the directory, you can use git.

(7. Press F8 to update the changes  when blender is running. Blender will reload the scripts.)

Cautions
-------

DONNOT CHANGE ANY NAMES OF THE TEMPLATE'S OBJECTS OR DELETE THEM.

ADD-ON DEPENDS ON THEM, SO IT WILL CAUSE FATAL ERROR TO YOUR SCENE.

UI
---

Installing the add-on will make a tab named 'BL2D' in the toolbar.

It has three panels, 'Info', 'Output', 'Cel', 'Indicators', 'Book'.

Only 'Info' and 'Output' is working now.

'Output' has two buttons; "Export Keyframes" and "Export full sheet preview".

"Export Keyframes" will export all of the keyframes in the cut.

"Export full sheet preview" will export the preview with border and aspect ratio iof 'Sheet'.


Scenes
------

There are three scenes in template: 'Main', 'TimeSheet', 'Preset_Lib'

'Main': Main working place. You will draw here.

'TimeSheet': Time sheet will be generated here.

'Preset_Lib': Some objects like indicators will be copied from here.

Objects
-------

There are many objects in the template.

Each one has its own rolls, add-on depends on them, so do not change their names or delete them.

Most of them might distact the user, and user might select and manipulate them by mistake.

So they are hidden or unselectable by default.

Camera
-------

There are three cameras in the scene "Main": "Camera_Main", "Camera_Scan_Frame", and "Camera_WholeSheet".

'Camera_Main': Default camera. The borders of the camera coreesponds to that of final screen.

'Camera_Scan_Frame': Same as scanframe, which is painting borderline in animation production. 

'Camera_WholeSheet': Corresponds to the whole sheet. Used to export keyframes.

Three cameras are hidden and unselectable at first, so you can't move them nor select them. 

But main and scanframe camera are parented to 'Camera_2dPanTBTU', so they will move along with them.

Moving it in the X and Y, camera will PAN, in Z it will TB or TU.

'Camera_WholeSheet' is parented to 'Sheet'. So even if the size of 'Sheet' changes, 'Camera_WholeSheet' will change with it.

Three cameras are orthographic by default, but you can change them to perspective.

However, it is not suitable to change 'Camera_WholeSheet' to perspective.
