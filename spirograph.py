import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed('fastest')
def spirograph(size_of_gaps):
    for _ in range(int(360 / size_of_gaps)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gaps)

spirograph(5)

screen = Screen()
screen.exitonclick()