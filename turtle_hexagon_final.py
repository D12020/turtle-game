# turtle 
# Saleem A
# 10.23.17

import time
import turtle
from random import randint
from turtle import*



size = 50
circles = 20
turtle.speed(.1)

turtle.colormode(255)

def red():
    color("green")
def green():
    color("red")
def blue():
    color("blue")
def yellow():
    color("yellow")

def up_arrow():
    forward(50)

def left_arrow():
    left(45)

def right_arrow():
    right(45)

def down_arrow():
    back(50)

listen()
onkeypress(red, "r")
onkeypress(green, "g")
onkeypress(blue, "b")
onkeypress(yellow, "y")
onkeypress(up_arrow, "Up")
onkeypress(left_arrow, "Left")
onkeypress(right_arrow, "Right")
onkeypress(down_arrow, "Down")


def move(length, angle):
                turtle.right(angle)
                turtle.forward(length)

def hex():
        turtle.pendown()
        turtle.color( randint(0,255),randint(0,255),randint(0,255) )
        turtle.begin_fill()
        for i in range(6):
                move(size,-60)
        turtle.end_fill()
        turtle.penup()

# start
turtle.penup()

for circle in range (circles):
        if circle == 0:
                hex()
                move(size,-60)
                move(size,-60)
                move(size,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (circle+1):
                        hex()
                        move(size,-60)
                        move(size,60)
                move(-size,0)
        move(-size,60)
        move(size,-120)
        move(0,60)
        time.sleep(0.1)


        

turtle.stop()
