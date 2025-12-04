# SUSHI/core/__init__.py
# Lazy-loaded wrapper: Fixes circular imports by deferring module loads to register()

import bpy
from bpy.utils import register_class, unregister_class

# No top-level imports here — that's the loop killer!
# We'll import inside functions only

def _lazy_import(name):
    """Safe import: Only loads when called, skips if already loaded."""
    if name in globals():
        return globals()[name]
    mod = __import__(name, fromlist=[''])
    globals()[name] = mod
    return mod

def register():
    # Register core classes first (safe, no imports needed)
    # Add any manual classes from Onigiri here if defined globally
    CLASSES = []  # Populate if you have explicit class defs; otherwise empty
    
    for cls in CLASSES:
        try:
            register_class(cls)
        except ValueError:
            pass  # Already registered
    
    # Now lazy-load and register modules (one by one, catch errors)
    MODULES_TO_REG = [
        'utils', 'animutils', 'devkit', 'gestures', 'rigutils',
        'collada', 'collada_universal', 'template_editor', 'views',
        # Add more as needed, but test incrementally
    ]
    
    for mod_name in MODULES_TO_REG:
        try:
            mod = _lazy_import(mod_name)
            if hasattr(mod, 'register'):
                mod.register()
        except ImportError as e:
            print(f"Warning: Failed to load {mod_name}: {e}")
        except Exception as e:
            print(f"Error registering {mod_name}: {e}")

def unregister():
    # Reverse order for safety
    MODULES_TO_UNREG = [
        'views', 'template_editor', 'collada_universal', 'collada',
        'rigutils', 'gestures', 'devkit', 'animutils', 'utils',
    ]
    
    for mod_name in reversed(MODULES_TO_UNREG):
        try:
            mod = _lazy_import(mod_name)
            if hasattr(mod, 'unregister'):
                mod.unregister()
        except:
            pass  # Graceful skip
    
    # Unregister classes last
    for cls in reversed(CLASSES):
        try:
            unregister_class(cls)
        except RuntimeError:
            pass

# For root loader compatibility — expose register/unregister
if __name__ == "__main__":
    register()