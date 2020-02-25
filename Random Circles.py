import turtle
import random
from turtle import *
# Draws 5 Random Circles and fills them with random colors from the list color
colors=['red','blue','black','green','orange','purple','violet','indigo','aqua','yellow']
turtle.speed(10)
for i in range(5):
    rand1=random.randrange(-300,200)
    rand2=random.randrange(-300,200)
    turtle.color(random.choice(colors),random.choice(colors))
    turtle.penup()
    turtle.goto(rand1,rand2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(random.randrange(10,100))
    turtle.end_fill()

turtle.mainloop()
