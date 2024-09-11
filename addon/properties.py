import bpy
from bpy.types import PropertyGroup, Scene, Object
from bpy.props import EnumProperty, PointerProperty, BoolProperty, StringProperty, IntProperty

from pathlib import Path


class MS_Data:
    splitter_system_path: Path = Path()
    splitter_system_enum: list = []

    def clear():
        cls = MS_Data
        cls.splitter_system_path: Path = Path()
        cls.splitter_system_enum: list = []



class MS_Properties(PropertyGroup):

    def get_splitter_systems(self, context):

        enum_items = []

        splitter_data: MS_Data = (context.scene.mesh_splitter_data)
        splitter_sys_dir = context.preferences.addons[__package__].preferences.assets_path

        # early exit if mesh splitter assets not available
        if not splitter_sys_dir: return enum_items

        path = Path(splitter_sys_dir)

        # early exit if mesh splitter assets path has not changed
        # if path == splitter_data.splitter_system_path: return splitter_data.splitter_system_enum


        print(f"Scanning directory: {path}")
        # crowds_data.crowd_system_path = path
        # for i, dir in enumerate(path.iterdir()):
        #     if not dir.is_dir():
        #         continue
        #     thumbnail_path = next(dir.glob("thumbnail.*"), None)
        #     thumbnail = "SYSTEM"
        #     if thumbnail_path:
        #         thumbnail = crowds_data.thumbnails.load_safe(
        #             dir.name.lower(), str(thumbnail_path), "IMAGE"
        #         ).icon_id
        #     enum_items.append(
        #         (dir.name, dir.name.capitalize(), "", thumbnail, i)
        #     )
        # crowds_data.crowd_system_enum = enum_items
        return enum_items

    is_splitter_mesh : BoolProperty(
        name = "Splitter Mesh",
        description = "Is Part Of Splitter Pipeline",
        default = False)

    splitter_system: EnumProperty(
        items= get_splitter_systems, name="Splitter System", description=""
    )


#--------------------------------------------------------- Registration
classes = [
    MS_Properties
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Scene.mesh_splitter_data = MS_Data()
    Scene.mesh_splitter = PointerProperty(type=MS_Properties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    # del Scene.mesh_splitter_data
    del Scene.mesh_splitter









#________________________________________________________________________ TMP

# class Procedural_Crowds_Data:
#     crowd_system_path: Path = Path()
#     crowd_system_enum: list = []
#     crowd_model_path: Path = Path()
#     crowd_model_enum: list = []
#     crowd_model_subcategorties_path: Path = Path()
#     crowd_model_subcategorties_enum: list = []
#     crowd_model_subcategorties_ui_name = "SubCategory"
#     crowd_animation_path: Path = Path()
#     crowd_animation_enum: list = []
#     model_categories_path: Path = Path()
#     model_categories_enum: list = []
#     model_subcategories_path: Path = Path()
#     model_subcategories_enum: list = []
#     model_subcategories_ui_name = "SubCategory"
#     model_lods_path: Path = Path()
#     model_lods_enum: list = []
#     model_lut: dict = {}
#     lookup_key = ""
#     animation_path: Path = Path()
#     animation_enum: list = []
#     thumbnails = previews.new(max_size=(128, 128))
#     is_update_tricked_down: bool = False

#     def clear():
#         cls = Procedural_Crowds_Data
#         cls.crowd_system_path: Path = Path()
#         cls.crowd_system_enum: list = []
#         cls.crowd_model_path: Path = Path()
#         cls.crowd_model_enum: list = []
#         cls.crowd_animation_path: Path = Path()
#         cls.crowd_animation_enum: list = []
#         cls.model_categories_path: Path = Path()
#         cls.model_categories_enum: list = []
#         cls.model_lut: dict = {}
#         cls.lookup_key = ""
#         cls.animation_path: Path = Path()
#         cls.animation_enum: list = []
#         cls.thumbnails.clear()
#         previews.remove(cls.thumbnails)
#         cls.thumbnails = previews.new(max_size=(128, 128))