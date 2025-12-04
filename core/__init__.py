# SUSHI/core/__init__.py
# Simple wrapper so the master Sushi loader can activate the legacy Onigiri code

import bpy
from . import (action_quats_to_euler, anim, animutils, axis_defs, bvh, collada,
               collada_universal, common, convert, curves, devkit, dynamic,
               edit, gestures, globals_py, hierarchy, icon, icon_defs,
               joint_data, latch, mapper, meshutils, mod_data, mod_flags,
               mod_functions, mod_settings, monitor, motion, onemap, pill,
               pose_bone_matrix, puppet, ragdoll, react, rigutils, shape,
               shifter, sim, slbvh, sliders, snap, splice, template_editor,
               templates, utils, views, visible)

# List of modules that have register/unregister functions
REGISTER_MODULES = [
    animutils, collada, collada_universal, devkit, gestures, rigutils,
    template_editor, utils, views  # add more if they exist
]

def register():
    for mod in REGISTER_MODULES:
        if hasattr(mod, "register"):
            mod.register()

def unregister():
    for mod in reversed(REGISTER_MODULES):
        if hasattr(mod, "unregister"):
            mod.unregister()