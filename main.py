import random
import turtle as t
from colors import color_set

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)

pos_x = -220
pos_y = -200

for _ in range(10):
    for _ in range(10):
        tim.teleport(pos_x, pos_y)
        tim.dot(20, random.choice(color_set))
        pos_x += 50
    pos_x = -220
    pos_y += 50

screen = t.Screen()
screen.exitonclick()