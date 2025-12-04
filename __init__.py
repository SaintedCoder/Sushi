# Sushi/__init__.py  ← ONLY FILE WE TOUCH
import bpy
from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "Sushi",
    "author": "SaintedCoder + community",
    "version": (0, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Sushi",
    "description": "Free open-source bento rigging tools (Onigiri 4.1.3 core)",
    "category": "Rigging",
}

# Import the real Onigiri core exactly how the original author did it
from .core import *

def register():
    core.register()

def unregister():
    core.unregister()