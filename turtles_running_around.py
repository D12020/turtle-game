import random
from turtle import *

Saleem = Turtle()
Marc = Turtle()
Anders = Turtle()
Annie = Turtle()

Saleem.shape("turtle")
Saleem.color("purple")

Annie.shape("turtle")
Annie.color("dodger blue")

Marc.shape("turtle")
Marc.color("black")

Anders.shape("turtle")
Anders.color("red")

Marc.forward(50)

for i in range(10):
    Anders.left(53)
    Saleem.right(36)
    Annie.right(45)
    Anders.forward(11)
    Saleem.forward(50)
    Annie.forward(27)

Marc.left(90)

all_turtles = [Saleem, Annie, Marc, Anders]

while True:
    for t in all_turtles:
        rand_dir = random.randint(-20,20)
        rand_dist = random.randint(5,10)

        t.right(rand_dir)
        t.forward(rand_dist)
