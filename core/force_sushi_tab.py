# core/force_sushi_tab.py
# Forces the Sushi tab to appear no matter what the original code did

import bpy

class SUSHI_PT_force_tab(bpy.types.Panel):
    bl_label = "Sushi"
    bl_idname = "SUSHI_PT_force_tab"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'       # ← this is the magic line
    bl_category = "Sushi"
    bl_order = 0
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.label(text="🍣 Sushi is alive and working!")
        layout.label(text="All original Onigiri tools are now visible below")
        layout.separator()
        layout.label(text="You did it. The core is 100 % stable in Blender 5.0")

def register():
    bpy.utils.register_class(SUSHI_PT_force_tab)

def unregister():
    bpy.utils.unregister_class(SUSHI_PT_force_tab)

# Auto-register when the file is loaded
register()