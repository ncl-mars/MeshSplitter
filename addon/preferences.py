import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty, EnumProperty


class MS_Preferences(AddonPreferences):
    bl_idname = __package__

    filepath: StringProperty(
        name="Assets Folder",
        subtype="DIR_PATH",
        description="Select Folder that contains Mesh Splitter Assets",
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Select Assets Folder")
        row.prop(self, "filepath", text="")



classes = [MS_Preferences]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
