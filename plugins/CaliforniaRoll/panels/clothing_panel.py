from bpy.types import Panel

class CALI_PT_clothing(Panel):
    bl_label = "California Roll"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sushi"

    def draw(self, context):
        layout = self.layout
        layout.operator("cali.fit_clothing", text="Fit Clothing to Body", icon='ARMATURE_DATA')
        layout.label(text="Select clothing → then body → click")

def register():
    bpy.utils.register_class(CALI_PT_clothing)

def unregister():
    bpy.utils.unregister_class(CALI_PT_clothing)