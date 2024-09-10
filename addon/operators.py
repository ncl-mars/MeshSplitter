import bpy
from bpy.types import Operator

import os
import sys

def get_assets_path(context):
    return context.preferences.addons[__package__].preferences.assets_path


class MS_OT_CreateSplitter(Operator):
    bl_idname = "mesh_splitter.create_splitter"
    bl_label = "Create Splitter"
    bl_description = "Create Mesh Splitter Pipeline"
    bl_options = {"REGISTER", "UNDO"}
    bl_context = "Scene"

    def execute(self, context):
        print("Creating splitter, Looking for assets at path : ", get_assets_path(context))
        
        return {'FINISHED'}


#--------------------------------------------------------- Registrations
classes = [
    MS_OT_CreateSplitter, 
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

