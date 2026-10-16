import math
def paint(height,width,cover):
    area=height*width
    no_of_cans=math.ceil(area/cover)   # new funtion is used (ceil)
    print(f"you will need {no_of_cans} cans of paint")
coverage=7 #(sqm)    
H=int(input("enter a wall height="))
w=int(input("enter a wall width="))
paint(height=H,width=w,cover=coverage)