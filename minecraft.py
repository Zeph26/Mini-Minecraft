from ursina import *
from ursina import Default, Vec3, scene
from ursina.color import white
from ursina.prefabs.first_person_controller import FirstPersonController
import random

from ursina.scene import instance as scene
from ursina.ursinastuff import Default
from ursina.vec3 import Vec3

app = Ursina()

sky = Sky()
player = FirstPersonController()

# variables
grass_texture = load_texture("Assets/Textures/Grass_Block.png")

stone_texture = load_texture("Assets/Textures/Stone_Block.png")

brick_texture = load_texture("Assets/Textures/Brick_Block.png")

dirt_texture = load_texture("Assets/Textures/Dirt_Block.png")

wood_texture = load_texture("Assets/Textures/Wood_Block.png")

sky_texture = load_texture("Assets/Textures/Skybox.png")

arm_texture = load_texture("Assets/Textures/Arm_Texture.png")

punch_sound = Audio("Assets/SFX/Punch_Sound.wav",loop=False,autoplay=False)

block_pick = 1

def update():
    global block_pick
    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.not_active()

    if held_keys["1"]:
        block_pick = 1
    if held_keys["2"]:
        block_pick = 2
    if held_keys["3"]:
        block_pick = 3
    if held_keys["4"]:
        block_pick = 4
    if held_keys["5"]:
        block_pick = 5
    



class Block(Button):
    def __init__(self, position = (0,0,0),texture = grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='Assets/Models/Block',
            texture=texture,
            origin_y=0.5,
            color=color.hsv(0, 0, random.uniform(0.9, 1.0)),
            highlight_color= color.lime,
            scale = 0.5
        )
    
    def input(self,key):
        if key == 'q' or key == 'escape':
            application.quit()
        if self.hovered :
            if key == "left mouse down":
                punch_sound.play()
                if block_pick == 1:
                    block = Block(position=self.position+mouse.normal, texture= grass_texture)
                if block_pick == 2:
                    block = Block(position=self.position+mouse.normal, texture= stone_texture)
                if block_pick == 3:
                    block = Block(position=self.position+mouse.normal, texture= brick_texture)
                if block_pick == 4:
                    block = Block(position=self.position+mouse.normal, texture= dirt_texture)
                if block_pick == 5:
                    block = Block(position=self.position+mouse.normal, texture= wood_texture)

            if key == "right mouse down":
                punch_sound.play()
                destroy(self)
                
class Hand(Entity):
    def   __init__(self):
        super().__init__(
            parent = camera.ui,
            model="Assets/Models/Arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150,-10,0),
            position = Vec2(0.4,-0.6)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def not_active(self):
        self.position = Vec2(0.4, -0.6)


for z in range(30):
    for x in range(30):
        Block(position=(x,0,z))

def input(key):
    if key == "q":
        application.quit()

hand = Hand()
app.run()