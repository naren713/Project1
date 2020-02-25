# Usings arrow keys to move
import turtle

t=turtle.Turtle()
def up():
    t.color(random.choice(colors))
    t.setheading(90)
    t.forward(100)

def down():
    t.color(random.choice(colors))
    t.setheading(270)
    t.forward(100)

def left():
    t.color(random.choice(colors))
    t.setheading(180)
    t.forward(100)

def right():
    t.color(random.choice(colors))
    t.setheading(0)
    t.forward(100)

def clickleft():
    t.stamp()

t.width(5)
t.speed(10)

t.listen()

t.onscreenclick(clickleft,1)

t.onkey(up,"Up")

t.onkey(down,"Down")

t.onkey(left,"Left")

t.onkey(right,"Right")

t.mainloop()
