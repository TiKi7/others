###################################################
# GUIDE@Tiki-8590                                 #
# ACTIVE OBJECT: IS THE SURROUNDING AREA          #
# OTHER SELECTED OBJECTS: ARE YOUR BUTTONS        #
###################################################
# Rsult Comes Here:
































































































































































































import bpy
from mathutils import *
from math import *

C = bpy.context
space = bpy.context.area.spaces.active
text = space.text
#bpy.ops.text.resolve_conflict(ctx, resolution='RELOAD')
bpy.ops.text.resolve_conflict(resolution='RELOAD')

C.selected_objects[0].data.vertices.values()

active  = C.active_object
width   = active.dimensions[0]
height  = active.dimensions[1]
offset  = Vector((width/2,-height/2,0))
fix_y   = Vector((1,-1,1))

events  = ''
data    = f'{width:.2f},{height:.2f},'

for obj in C.selected_objects:
    if obj==active: continue
    
    p1 = None
    p2 = None
    for v in obj.data.vertices:
        co = obj.matrix_world @ v.co
        co = co + offset
        co = co * fix_y
        if(p1==None): p1=co
        if(p2==None): p2=co
        if(co<p1): p1=co
        if(co>p2): p2=co
    #now use our data to our liking...
    events += f'{obj.name},'
    data += f'{p1.x:.2f},{p1.y:.2f},{p2.x:.2f},{p2.y:.2f},' 

output = ''
output += '\n"""'

output += '\n\n// TheWall: <Events>'
output += f'\n{events}'

output += '\n\n// TheWall: <Data>'
output += f'\n{data}'

output += '\n\n"""'


bpy.ops.text.jump(line=7)
#bpy.ops.text.move(type='LINE_BEGIN')
#text.write('')
text.write(output)