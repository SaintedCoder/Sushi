# Sushi – Emerald Works 2026
bl_info = {
    "name": "Sushi",
    "author": "Emerald Works",
    "version": (0, 9, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Sushi",
    "description": "The free forever Bento replacement",
    "category": "Rigging",
}

import bpy
from .core import register as register_core, unregister as unregister_core
from .plugins.CaliforniaRoll import register as register_california, unregister as unregister_california

modules = (
    register_core,
    register_california,
)

def register():
    for m in modules:
        m()

def unregister():
    for m in reversed(modules):
        m()

if __name__ == "__main__":
    register()