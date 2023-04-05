print(extractName)
import bpy
#bpy.ops.object.duplicate()
#bpy.ops.outliner.item_rename('as')
sel = bpy.context.selected_objects
for i in range(len(sel)):
    #print(bpy.context.selected_objects[i].name)
    print(i)
    oldName = bpy.context.selected_objects[i].name
    newName = oldName.replace('_', '-')
    bpy.context.selected_objects[i].name = newName