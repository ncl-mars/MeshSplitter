#************************************************************************************
# Since reloading addon in vscode (using jacques lucke ext) resets properties, 
# I use a debug variable and a root folder name ("MeshSplitter") to look for a 
# default assets folder at ./MeshSplitter/assets

#************************************************************************************

import bpy
from bpy.types import AddonPreferences, Operator
from bpy.props import StringProperty, EnumProperty, IntProperty, BoolProperty

from pathlib import Path
import os

from . import globals


# for debug/dev mode purposes !
def get_default_assets_path():

    _path = ""

    if globals.DEBUG == False : return _path # if not in debug mode, return empty string

    for parent in Path(__file__).parents :
        if parent.name == "MeshSplitter":
            _assets_path = parent.joinpath("assets")

            if _assets_path.exists() :
                _path = str(_assets_path)
                print("setting default assets path : ", _path)

    return _path


#--------------------------------------------------------- Preferences
class MS_Preferences(AddonPreferences):

    bl_idname = __package__

    assets_path: StringProperty(
        name="Assets Folder",
        subtype="DIR_PATH",
        description="Select Folder that contains Mesh Splitter Assets",
        default = get_default_assets_path()
    )


    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Select Assets Folder")
        row.prop(self, "assets_path", text="")


#--------------------------------------------------------- Registration
classes = [
    MS_Preferences,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)












#________________________________________________________________________ TMP

# addon_prefs = bpy.context.preferences.addons[__package__].preferences 
# if os.path.exists(addon_prefs.assets_path) :
#     addon_prefs.assets_loaded = True

# assets_loaded : BoolProperty(
#     name="Assets Folder",
#     default = False
# )

# self["assets_loaded"] = os.path.exists(self["assets_path"])

# class MS_OT_CheckAssets(Operator):
    
#     bl_idname = "mesh_spliiter.check_assets"
#     bl_label = "Check For Loaded Assets"
#     bl_options = {'REGISTER', 'UNDO'}

#     @classmethod
#     def poll(cls, context):
#         print("polling preferences")
#         return context.object is not None

#     def init(self):
#         print("init")
