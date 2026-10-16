weight=int(input("enter your weight in kg="))
height=float(input("enter your height in cm="))
height=height/100
BMI=weight/(height**2)
print("body mass index is=",round(BMI))
if(BMI<18):
    {
        print("under weight")
    }
elif(BMI<25):
    {
        print("normal weight")
    }
elif(BMI<30):
    {
        print("over weight")
    }
else:
    {
        print("obese")
    }
