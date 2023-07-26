from random import randint
import pgzrun

class Player(Actor):
    speed= 5
    

#player control
    if keyboard.left:
        p.x -= ps
    if keyboard.right:
        p.x += ps
    if keyboard.up:
        p.y -= ps
    if keyboard.down:
        p.y += ps 
    if keyboard.space:
        p.angle += ps 
class Enemy(Actor):
    speed= 2

class Friut(Actor):
    pass

Player.speed
