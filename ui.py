import bpy

# Function Definitions ############################################################################################
def create_morning_light():
        bpy.ops.object.light_add(type='SUN')
        new_light = bpy.context.object
        new_light.name = "Morning"
        new_light.data.energy = 2.0
        new_light.data.color = (1,0.2,0)
        new_light.rotation_euler = (0, -1.5708, 0)
        
def create_midday_light():      
        bpy.ops.object.light_add(type='SUN')
        new_light = bpy.context.object
        new_light.name = "Midday"
        new_light.data.energy = 2.0
        new_light.data.color = (1,1,0.5)
        new_light.rotation_euler = (0, 0, 0)
     
def create_afternoon_light():
        bpy.ops.object.light_add(type='SUN')
        new_light = bpy.context.object
        new_light.name = "Afternoon"
        new_light.data.energy = 2.0
        new_light.data.color = (1,0.2,0.2)
        new_light.rotation_euler = (0, 1.5708, 0)
def create_midnight_light():

        bpy.ops.object.light_add(type='SUN')
        new_light = bpy.context.object
        new_light.name = "Midnight"
        new_light.data.energy = 2.0
        new_light.data.color = (0.3,0.7,1)
        new_light.rotation_euler = (0, 0, 0)
        
        
def clear():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='LIGHT')
    bpy.ops.object.delete()
    
def image_phone():
    bpy.context.scene.render.resolution_x = 1080
    bpy.context.scene.render.resolution_y = 1920
    bpy.context.scene.render.pixel_aspect_x = 9
    bpy.context.scene.render.pixel_aspect_y = 16
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'
    bpy.context.scene.render.image_settings.compression = 100
    
def image_fullhd():
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.pixel_aspect_x = 16
    bpy.context.scene.render.pixel_aspect_y = 9
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'
    bpy.context.scene.render.image_settings.compression = 100
    
def image_4k():
    bpy.context.scene.render.resolution_x = 3840
    bpy.context.scene.render.resolution_y = 2160
    bpy.context.scene.render.pixel_aspect_x = 16
    bpy.context.scene.render.pixel_aspect_y = 9
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'
    bpy.context.scene.render.image_settings.compression = 100
    
def image_a4():
    bpy.context.scene.render.resolution_x = 2480
    bpy.context.scene.render.resolution_y = 3508
    bpy.context.scene.render.pixel_aspect_x = 1
    bpy.context.scene.render.pixel_aspect_y = 1
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'
    bpy.context.scene.render.image_settings.compression = 100
    
def video_fullhd():
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.pixel_aspect_x = 16
    bpy.context.scene.render.pixel_aspect_y = 9
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.image_settings.color_mode = 'RGB'
    bpy.context.scene.render.image_settings.compression = 100
    
def video_4k():
    bpy.context.scene.render.resolution_x = 3840
    bpy.context.scene.render.resolution_y = 2160
    bpy.context.scene.render.pixel_aspect_x = 16
    bpy.context.scene.render.pixel_aspect_y = 9
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.image_settings.color_mode = 'RGB'
    bpy.context.scene.render.image_settings.compression = 100
    
def video_8k():
    bpy.context.scene.render.resolution_x = 7680
    bpy.context.scene.render.resolution_y = 4320
    bpy.context.scene.render.pixel_aspect_x = 16
    bpy.context.scene.render.pixel_aspect_y = 9
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.image_settings.color_mode = 'RGB'
    bpy.context.scene.render.image_settings.compression = 100

# Panel Config ###############################################################################################################
class SimplePanel(bpy.types.Panel):
    bl_label = "Light Presets"
    bl_idname = "OBJECT_PT_panel_1"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jorge'
        
    def draw(self, context):
        layout = self.layout
        
        col = layout.column()
        col.label(text="Day Lights:")
        box = col.box()
            
        row = box.row()
        row.operator("object.button_operator1", text="Morning")

        row = box.row()
        row.operator("object.button_operator2", text="Midday")

        row = box.row()
        row.operator("object.button_operator3", text="Afternoon")

        row = box.row()
        row.operator("object.button_operator4", text="Midnight")
        
        col = layout.column()
        col.label(text="Clear:")
        box = col.box()
        row = box.row()
        row.operator("object.button_operator5", text="Clear all lights")
        
        col = layout.column()
        col.label(text="Intensity:")
        box = col.box()
        row = box.row()
            
        if context.object and context.object.type == 'LIGHT':
            intensity = context.object.data
            rotation = context.object
            row.prop(intensity, "energy", text="Intensity")
            row = box.row()
            row.prop(rotation, "rotation_euler", index=0 , text = "X Rotation")
            row = box.row()
            row.prop(rotation, "rotation_euler", index=1 , text = "Y Rotation")
            
        else:
            row.label(text="Select a Light to change")
            row = box.row()
            row.label(text="it's intensity and rotation.")
            
# Panel 2 Config #############################################################################################################
class SimplePanel2(bpy.types.Panel):
    bl_label = "Render Presets"
    bl_idname = "OBJECT_PT_panel_2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jorge'

    def draw(self, context):
        layout = self.layout
        
        col = layout.column()
        col.label(text="Image Presets")
        box = col.box()
            
        row = box.row()
        row.operator("object.button_operator6", text="Phone Wallpaper")
            
        row = box.row()
        row.operator("object.button_operator7", text="16x9 FullHD")
            
        row = box.row()
        row.operator("object.button_operator8", text="16X9 4K")
            
        row = box.row()
        row.operator("object.button_operator9", text="A4 Print")

        col = layout.column()
        col.label(text="Video Presets")
        box = col.box()
            
        row = box.row()
        row.operator("object.button_operator10", text="16x9 FullHD")
            
        row = box.row()
        row.operator("object.button_operator11", text="16X9 4K")
            
        row = box.row()
        row.operator("object.button_operator12", text="16X9 8k")

# Button Registration ########################################################################################################
class Button1Operator(bpy.types.Operator):
    bl_idname = "object.button_operator1"
    bl_label = "Morning"

    def execute(self, context):
        create_morning_light()
        return {'FINISHED'}
    
class Button2Operator(bpy.types.Operator):
    bl_idname = "object.button_operator2"
    bl_label = "Midday"

    def execute(self, context):
        create_midday_light()
        return {'FINISHED'}
    
class Button3Operator(bpy.types.Operator):
    bl_idname = "object.button_operator3"
    bl_label = "Afternoon"

    def execute(self, context):
        create_afternoon_light()
        return {'FINISHED'}
    
class Button4Operator(bpy.types.Operator):
    bl_idname = "object.button_operator4"
    bl_label = "Midnight"

    def execute(self, context):
        create_midnight_light()
        return {'FINISHED'}

class Button5Operator(bpy.types.Operator):
    bl_idname = "object.button_operator5"
    bl_label = "Clear all lights"

    def execute(self, context):
        clear()
        return {'FINISHED'}
    
class Button6Operator(bpy.types.Operator):
    bl_idname = "object.button_operator6"
    bl_label = "Phone Wallpaper"

    def execute(self, context):
        image_phone()
        return {'FINISHED'}
    
class Button7Operator(bpy.types.Operator):
    bl_idname = "object.button_operator7"
    bl_label = "16x9 FullHD"

    def execute(self, context):
        image_fullhd()
        return {'FINISHED'}
    
class Button8Operator(bpy.types.Operator):
    bl_idname = "object.button_operator8"
    bl_label = "16x9 4K"

    def execute(self, context):
        image_4k()
        return {'FINISHED'}
    
class Button9Operator(bpy.types.Operator):
    bl_idname = "object.button_operator9"
    bl_label = "A4 Print"

    def execute(self, context):
        image_a4()
        return {'FINISHED'}
    
class Button10Operator(bpy.types.Operator):
    bl_idname = "object.button_operator10"
    bl_label = "16x9 FullHD"

    def execute(self, context):
        video_fullhd()
        return {'FINISHED'}
    
class Button11Operator(bpy.types.Operator):
    bl_idname = "object.button_operator11"
    bl_label = "16x9 4K"

    def execute(self, context):
        video_4k()
        return {'FINISHED'}
    
class Button12Operator(bpy.types.Operator):
    bl_idname = "object.button_operator12"
    bl_label = "16x9 8K"

    def execute(self, context):
        video_8k()
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(SimplePanel2)
    bpy.utils.register_class(Button1Operator)
    bpy.utils.register_class(Button2Operator)
    bpy.utils.register_class(Button3Operator)
    bpy.utils.register_class(Button4Operator)
    bpy.utils.register_class(Button5Operator)
    bpy.utils.register_class(Button6Operator)
    bpy.utils.register_class(Button7Operator)
    bpy.utils.register_class(Button8Operator)
    bpy.utils.register_class(Button9Operator)
    bpy.utils.register_class(Button10Operator)
    bpy.utils.register_class(Button11Operator)
    bpy.utils.register_class(Button12Operator)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(SimplePanel2)
    bpy.utils.unregister_class(Button1Operator)
    bpy.utils.unregister_class(Button2Operator)
    bpy.utils.unregister_class(Button3Operator)
    bpy.utils.unregister_class(Button4Operator)
    bpy.utils.unregister_class(Button5Operator)
    bpy.utils.unregister_class(Button6Operator)
    bpy.utils.unregister_class(Button7Operator)
    bpy.utils.unregister_class(Button8Operator)
    bpy.utils.unregister_class(Button9Operator)
    bpy.utils.unregister_class(Button10Operator)
    bpy.utils.unregister_class(Button11Operator)
    bpy.utils.unregister_class(Button12Operator)

if __name__ == "__main__":
    register()
