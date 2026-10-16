import turtle
import random
turtle.colormode(255)
t=turtle.Turtle()
#t.pencolor("red")
t.speed("fastest")
t.color("red","yellow")
t.begin_fill()
while True:
    t.fd(300)
    t.lt(170)
    if t.heading()==0:
        break
t.end_fill()    
t.screen.mainloop()    
