import random
from turtle import Turtle
t=Turtle()
list=["red","black","orange","green","blue","yellow","bisque2","blue violet","burlywood3","chocolate","cyan3","dark blue","dark magenta ","DarkGoldenrod3","DarkOrchid1","DarkSlateBlue","deep sky blue","firebrick4","gold","gray56","GreenYellow","LavenderBlush1","LawnGreen","light coral","medium orchid","medium purple","MediumAquamarine","old lace","OrangeRed","peach puff","SeaGreen4"]
edges=3
t.width(1)
for _ in range(6):
    angle=360//edges
    t.pencolor(random.choice(list))
    for i in range(edges):
        t.fd(70)
        t.rt(angle)
    edges+=1    