import turtle
import random
turtle.colormode(255)
t=turtle.Turtle()
#list=["red","black","orange","green","blue","yellow","bisque2","blue violet","burlywood3","chocolate","cyan3","dark blue","dark magenta ","DarkGoldenrod3","DarkOrchid1","DarkSlateBlue","deep sky blue","firebrick4","gold","gray56","GreenYellow","LavenderBlush1","LawnGreen","light coral","medium orchid","medium purple","MediumAquamarine","old lace","OrangeRed","peach puff","SeaGreen4"]
t.width(5)
t.shape("turtle")
t.speed("fastest")
for _ in range(200):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.setheading(random.randrange(0,360,90))
    t.pencolor((r,g,b))
    t.fd(40)
t.screen.mainloop()    