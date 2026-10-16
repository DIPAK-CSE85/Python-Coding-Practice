import turtle
import random
turtle.colormode(255)
t=turtle.Turtle()
#list=["red","black","orange","green","blue","yellow","bisque2","blue violet","burlywood3","chocolate","cyan3","dark blue","dark magenta ","DarkGoldenrod3","DarkOrchid1","DarkSlateBlue","deep sky blue","firebrick4","gold","gray56","GreenYellow","LavenderBlush1","LawnGreen","light coral","medium orchid","medium purple","MediumAquamarine","old lace","OrangeRed","peach puff","SeaGreen4"
t.shape("circle")
t.speed("fastest")
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.pencolor((r,g,b))
    t.circle(150)
    t.lt(1)
    if t.heading()==0:
        break
turtle.exitonclick()