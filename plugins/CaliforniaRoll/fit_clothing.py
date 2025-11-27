from bpy.types import Operator

class CALI_OT_fit_clothing(Operator):
    bl_idname = "cali.fit_clothing"
    bl_label = "Fit to Body"

    def execute(self, context):
        clothing = context.selected_objects[0]
        body = context.selected_objects[1] if len(context.selected_objects) > 1 else None
        if not body:
            self.report({'ERROR'}, "Select clothing first, then body")
            return {'CANCELLED'}

        # One-click shrinkwrap + weight copy
        mod = clothing.modifiers.new(name="Shrinkwrap", type='SHRINKWRAP')
        mod.target = body
        mod.wrap_method = 'PROJECT'
        mod.use_negative_direction = True
        bpy.ops.object.modifier_apply(modifier="Shrinkwrap")

        # Copy weights from body
        bpy.ops.object.data_transfer(
            use_reverse_transfer=False,
            data_type='VGROUP',
            use_object_transform=True,
            layers_select_src='NAME',
            layers_select_dst='ACTIVE'
        )
        self.report({'INFO'}, f"{clothing.name} fitted to {body.name}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(CALI_OT_fit_clothing)

def unregister():
    bpy.utils.unregister_class(CALI_OT_fit_clothing)