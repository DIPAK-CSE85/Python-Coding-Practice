#simple while loop
count=1
while count<=5:
    print(count)
    count+=1

    
#while else condition
count=1
while count<=5:
    print(count)
    count+=1
    if(count==4):
        break
else:
    print("successfully execute") 
print("end of loop")       



# program that find the sum of numbers and quite from program by enter 0 or -1
number=int(input("enter a number(0 or -1 for quite)"))
sum=0
while number!=0 and number!=-1:
    sum+=number
    number=int(input("enter a number(0 or -1 for quite)"))
else:
    print("successfully execute")  
print("end of loop")  
print(sum)

