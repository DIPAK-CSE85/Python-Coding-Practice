from turtle import *
import random
s1=Screen()
tom=Turtle()
colormode(255)
tom.width(3)
s1.bgcolor("black")
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.pencolor((r,b,g))
    def up():
        tom.setheading(90)
        tom.fd(10)
    def left():
        tom.setheading(180)
        tom.fd(10)
    def down():
        tom.setheading(270)
        tom.fd(10)
    def right():
        tom.setheading(0)
        tom.fd(10) 
    def clear_screen():
        tom.clear()
        tom.pu()
        tom.home()
        tom.pd()
    def delete():
        tom.clear()
    s1.listen()   
    s1.onkey(fun=up,key="Up")    
    s1.onkey(fun=right,key="Right")
    s1.onkey(fun=left,key="Left")
    s1.onkey(fun=down,key="Down")
    s1.onkey(fun=clear_screen,key="c")
    s1.onkey(fun=delete,key="x")
s1.exitonclick()
