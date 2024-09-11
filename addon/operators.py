import bpy
from bpy.types import Operator

import os
import sys


def get_assets_path(context):
    return context.preferences.addons[__package__].preferences.assets_path


class MS_OT_CreateSplitter(Operator):
    bl_idname = "mesh_splitter.create_splitter"
    bl_label = "Split Mesh"
    bl_description = "Create Mesh Splitter Pipeline"
    bl_options = {"REGISTER", "UNDO"}
    bl_context = "Scene"


    def execute(self, context):
        
        scene = context.scene
        props = scene.mesh_splitter

        splitter_systems = props.splitter_system

        
        
        if len(context.selected_objects) < 1 : return {'CANCELLED'}

        # active_object = context.selected_objects[0]
        # is_splitter = active_object.mesh_splitter.is_splitter_mesh
        # if is_splitter : print("selected mesh is already being split")
        # else :
        #     print("selected object is splitter : " + str(is_splitter))
        #     active_object.mesh_splitter.is_splitter_mesh = True

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




# print("Creating splitter, Looking for assets at path : ", get_assets_path(context))