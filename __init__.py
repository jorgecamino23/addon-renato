bl_info = {
        "name": "Addon Jorge",
        "description": "Addon created for Renato.",
        "author": "Jorge Camino",
        "version": (1, 0),
        "blender": (3, 5, 0),
        "location": "3D View > Side Panel > Jorge",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "",
        "tracker_url": "",
        "support": "COMMUNITY",
        "category": "3D View"
        }

import bpy

def register():
    from . import ui
    ui.register()

def unregister():
    from . import ui
    ui.unregister()

if __name__ == '__main__':
    register()
