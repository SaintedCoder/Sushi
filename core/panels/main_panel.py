from bpy.types import Panel

class SUSHI_PT_main(Panel):
    bl_label = "Sushi"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sushi"

    def draw(self, context):
        layout = self.layout
        layout.operator("sushi.export_mesh", text="Export Mesh (dae + glb)", icon='EXPORT')
        layout.separator()
        layout.label(text="California Roll → Active")
        layout.label(text="Fugu → Coming soon")
        layout.label(text="Free forever. Paid modules optional.")

def register():
    bpy.utils.register_class(SUSHI_PT_main)

def unregister():
    bpy.utils.unregister_class(SUSHI_PT_main)