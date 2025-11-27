import bpy
from bpy.types import Operator

class SUSHI_OT_export_mesh(Operator):
    bl_idname = "sushi.export_mesh"
    bl_label = "Export Mesh"
    bl_options = {'REGISTER'}

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Select a mesh first")
            return {'CANCELLED'}

        # Uses our fixed Godot Collada + glTF packers
        bpy.ops.export_scene.collada(filepath="C:/temp/test.dae", use_selection=True)
        bpy.ops.export_scene.glb(filepath="C:/temp/test.glb", use_selection=True, export_format='GLB')
        self.report({'INFO'}, "Exported .dae + .glb to C:/temp/")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SUSHI_OT_export_mesh)

def unregister():
    bpy.utils.unregister_class(SUSHI_OT_export_mesh)