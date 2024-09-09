import bpy



#--------------------------------------------------------- Main Panel
class View3DPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mesh Splitter"
    bl_label = "Mesh Splitter"
    bl_idname = "VIEW3D_PT_ms_viewport"


    def draw(self, context):
        scene = context.scene
        layout = self.layout
        row = layout.row()
        row.label(text= "Init Text (First Commit)")
        



#--------------------------------------------------------- Registrations
classes = [
    View3DPanel, 
]

def init():
    print("!! -> initializing mesh_splitter")


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
