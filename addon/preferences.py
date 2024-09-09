# # https://blenderartists.org/t/addon-preferences-saving-global-variable/1464471/3

import bpy
from bpy.types import AddonPreferences, Operator
from bpy.props import StringProperty, EnumProperty, IntProperty, BoolProperty



from pathlib import Path

default_assets_path = Path(__file__).parent

#--------------------------------------------------------- Preferences
class MS_Preferences(AddonPreferences):
    bl_idname = __package__

    filepath: StringProperty(
        name="Assets Folder",
        subtype="DIR_PATH",
        description="Select Folder that contains Mesh Splitter Assets",
        # default = "./
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Select Assets Folder")
        row.prop(self, "filepath", text="")



classes = [
    MS_Preferences
]

def register():
    print("!! -> registering mesh splitter addon preferences")
    print("!! -> This is a breaking Test")

    print("Default assets path :" , default_assets_path)

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)








# os.path.realpath(os.path.expanduser("~/botaniq_animations/"))

# class MS_OT_Preferences(Operator):
#     """Display example preferences"""
#     bl_idname = "mesh_splitter.addon_prefs"
#     bl_label = "Add-on Preferences"
#     bl_options = {'REGISTER', 'UNDO'}

#     def execute(self, context):
#         preferences = context.preferences
#         addon_prefs = preferences.addons[__name__].preferences

#         info = "filepath: {:s}".format(
#             addon_prefs.filepath
#         )
#         self.report({'INFO'}, info)
#         print(info)

#         return {'FINISHED'}

