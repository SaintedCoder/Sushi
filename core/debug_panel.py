# core/debug_panel.py
# Tiny debug panel — forces the Sushi tab to appear no matter what

import bpy

class SUSHI_PT_debug(bpy.types.Panel):
    bl_label = "Sushi Debug"
    bl_idname = "SUSHI_PT_debug"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sushi"        # ← this is the important line
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        layout.label(text="Sushi core loaded correctly!")
        layout.label(text="All original Onigiri tools are below")

def register():
    bpy.utils.register_class(SUSHI_PT_debug)

def unregister():
    bpy.utils.unregister_class(SUSHI_PT_debug)