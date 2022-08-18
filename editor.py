from ursina import *

app = Ursina()
EditorCamera()#  NOTE: you need to remove this if you have any other camera setting working
window.title='Position Editor'

e = Entity(model='cube', texture='white_cube',y=1,color=color.orange) # example Entity
e2=Entity(model='cube', texture='white_cube',y=-1, scale=(10,1,10,), texture_scale=(2,2,2))#Example floor







target = e 						# set the entity here, example:- target = your_entity_name
entity_move_speed = 0.06        #edit this according to your need
# 				 NOTE: you need to remove *EditorCamera()* if you have any other camera setting(s)








target_yText= Text(text= str(target.y), scale=2, color=color.green, position=(0.7,0.05))
target_y = str(round(target.y))

target_zText= Text(text= str(target.z), scale=2, color=color.azure, position=(0.7,-0.05))
target_z = str(round(target.z))

target_xText= Text(text= str(target.x), scale=2, color=color.red, position=(0.7,0))
target_x = str(round(target.x))


#image
#img = Entity(model='quad', texture='assets/3d_axis', parent=camera.ui, position=(0.7,0.2), scale=0.3)

def update():
	global target_y
	target_y = target.y
	target_yText.text= str(target.y)

	global target_z
	target_z = target.z
	target_zText.text= str(target.z)

	global target_x
	target_x = target.x
	target_xText.text= str(target.x)

	if held_keys['up arrow']:
		target.position += target.up * entity_move_speed

	if held_keys['down arrow']:
		target.position += target.down * entity_move_speed

	if held_keys['a']:
		target.position += target.left * entity_move_speed

	if held_keys['d']:
		target.position += target.right * entity_move_speed

	if held_keys['w']:
		target.position += target.forward * entity_move_speed

	if held_keys['s']:
		target.position += target.back * entity_move_speed


app.run()
