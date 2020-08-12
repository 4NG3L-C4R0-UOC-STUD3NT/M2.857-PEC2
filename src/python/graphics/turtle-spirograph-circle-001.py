import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize(2)
t.speed(0)

for i in range(6):
    for color in ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']:
        t.color(color)
        t.circle(100)
        t.left(10)

time.sleep(15)

t.hideturtle()
turtle.done()

time.sleep(15)
