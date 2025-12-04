# SUSHI/__init__.py
import os
import importlib
import bpy

bl_info = {
    "name": "Sushi",
    "author": "The Sushi Team",
    "version": (0, 1, 0),
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Sushi",
    "description": "Free, open-source bento rigging and animation tools for Second Life / OpenSim",
    "category": "Rigging",
}

modules = ["core"]

# Auto-discover plugin folders
plugin_path = os.path.join(os.path.dirname(__file__), "plugins")
if os.path.exists(plugin_path):
    for name in sorted(os.listdir(plugin_path)):
        full = os.path.join(plugin_path, name)
        if os.path.isdir(full) and not name.startswith("_"):
            modules.append(f"plugins.{name}")

def register():
    for m in modules:
        mod = importlib.import_module(f".{m}", package=__package__)
        if hasattr(mod, "register"):
            mod.register()

def unregister():
    for m in reversed(modules):
        mod = importlib.import_module(f".{m}", package=__package__)
        if hasattr(mod, "unregister"):
            mod.unregister()