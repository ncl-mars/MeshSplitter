import bpy
from bpy.types import PropertyGroup, Scene, Object

from bpy.props import (
    EnumProperty,
    PointerProperty,
    BoolProperty,
    StringProperty,
    IntProperty,
)





class MS_Properties(PropertyGroup):
    is_splitter_mesh : bpy.props.BoolProperty(
    name = "isSplitterMesh",
    description = "Is Part Of Splitter Pipeline",
    default = False)





#--------------------------------------------------------- Registration
classes = [
    MS_Properties
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    Scene.mesh_splitter = PointerProperty(type=MS_Properties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    del Scene.mesh_splitter
