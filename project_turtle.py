import random
from turtle import Turtle,Screen
width,height=400,400
list=["red","black","orange","green","blue","yellow","bisque2","blue violet","burlywood3","chocolate","cyan3","dark blue","dark magenta ","DarkGoldenrod3","DarkOrchid1","DarkSlateBlue","deep sky blue","firebrick4","gold","gray56","GreenYellow","LavenderBlush1","LawnGreen","light coral","medium orchid","medium purple","MediumAquamarine","old lace","OrangeRed","peach puff","SeaGreen4"]
def turtles():
    while True:
       t=int(input("how may turtle you want(2_10)="))
       if 2<=t<=10:
            return t
       else:
           print("you enter wrong option plese try again")     
t=turtles()
s1=Screen()
s1.setup(400,400)
x_part=width//(t+1)      
turtle_list=[]           
for i in range(1,t+1):
    new_t=Turtle()
    new_t.shape("turtle")
    new_t.fillcolor(list[i-1])
    new_t.lt(90)
    new_t.pu()
    new_t.goto(-400//2+(x_part*i),(-400/2)+10)
    turtle_list.append(new_t)
def race():
    is_race_on=True
    while is_race_on:
        for turtle in turtle_list:
            distance=random.randint(1,20)
            turtle.fd(distance)
            x,y=turtle.pos()
            if y>=height//2:
                print(f"the winner is {turtle.fillcolor()} turtle")
                is_race_on=False
race()                
s1.mainloop()            
