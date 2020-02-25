from turtle import *
import turtle

def dragging(x,y):
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x,y))
    turtle.goto(x,y)
    turtle.ondrag(dragging)

def clickright(x,y):
    turtle.clear()


def main():
    turtle.listen()

    turtle.ondrag(dragging)

    turtle.onscreenclick(clickright,3)

    turtle.mainloop()

turtle.speed(-1)
turtle.shape("turtle")
turtle.width(2)
main()