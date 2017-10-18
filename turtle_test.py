from turtle import *
def draw_star(x, y, points, size, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(points):
        forward(size)
        left(turn)
    end_fill()

def draw_tree(x, y):
    penup()
    goto(x, y)
    pendown()

    color(line, fill)

    begin_fill()
    for i in range(points):
        forward(100)
        left(90)
        left(45)
        forward(20)
        right(45)
        forward(5)
        right(45)
        forward(20)
        
    end_fill()

    
    
speed(40)


draw_star(-150, 0, 60, 100, "light green", "green")
draw_star(-100, 0, 60, 100, "dark green", "sea green")
draw_star(-50, 0, 60, 100, "dark sea green", "green")
draw_star(100, 0, 60, 100, "green", "dark sea green")
draw_star(150, 0, 60, 100, "sea green", "dark green")
draw_star(200, 0, 60, 100, "green","light green")
draw_tree(0,50)




done()
