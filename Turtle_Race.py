from turtle import *
import turtle
import random
colors=['red','blue','purple','yellow']


r1=random.randrange(450,500)
r2=random.randrange(450,500)
r3=random.randrange(450,500)
r4=random.randrange(450,500)

t1=Turtle()
t1.hideturtle()
t1.shape("turtle")
t1.color(random.choice(colors))
t1.penup()
t1.setpos(-250,-200)
t1.pendown()
t1.showturtle()
t1.setheading(90)
t1.speed(random.randrange(3,6))

t2=Turtle()
t2.hideturtle()
t2.shape("turtle")
t2.color(random.choice(colors))
t2.penup()
t2.setpos(-200,-200)
t2.pendown()
t2.showturtle()
t2.setheading(90)
t2.speed(random.randrange(3,6))


t3=Turtle()
t3.hideturtle()
t3.shape("turtle")
t3.color(random.choice(colors))
t3.penup()
t3.setpos(-150,-200)
t3.pendown()
t3.showturtle()
t3.setheading(90)
t3.speed(random.randrange(3,6))

t4=Turtle()
t4.hideturtle()
t4.shape("turtle")
t4.color(random.choice(colors))
t4.penup()
t4.setpos(-100,-200)
t4.pendown()
t4.showturtle()
t4.setheading(90)
t4.speed(random.randrange(3,6))



t1.fd(r1)
t2.fd(r2)
t3.fd(r3)
t4.fd(r4)


turtle.mainloop()
