import turtle
import random
turtle.colormode(255)
t=turtle.Turtle()
t.shape("circle")
t.speed("fastest")
for _ in range(1000):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.setheading(random.randrange(0,360))
    t.color((r,g,b),(r,g,b))
    t.begin_fill()
    t.circle(7)
    t.end_fill()
    t.pu()
    t.fd(100)
    t.pd()
t.screen.mainloop()