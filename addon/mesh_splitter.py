import bpy



#--------------------------------------------------------- Main Panel
class MS_ViewPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mesh Splitter"
    bl_label = "Mesh Splitter"
    bl_idname = "MS_PT_view_panel"


    def draw(self, context):
        scene = context.scene
        layout = self.layout
        row = layout.row()
        row.label(text= "Init Text (First Commit)")
        



#--------------------------------------------------------- Registrations
classes = [
    MS_ViewPanel, 
]

# def init():
#     print("!! -> initializing viewport GUI")


def register():
    print("!! -> registering viewport gui")
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
