import turtle

def petal(r,l,angle):
    for i in range(2):
        turtle.circle(r,angle)
        turtle.lt(180-angle)

# petal(60,60,60)

def flower(r,n,l,angle):
    for i in range(n):
        petal(r,l,angle)
        turtle.lt(360/n)

# flower(60,7,60,60)

# turtle.goto(-250.0)
turtle.speed(50)
turtle.color("blue")
flower(50,30,30,80)

turtle.mainloop()