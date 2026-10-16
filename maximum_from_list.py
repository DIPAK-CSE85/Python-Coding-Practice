numbers=input("enter the numbers seperated by a comma=")
numbers_list=numbers.split(",")
for i in range(len(numbers_list)):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)
maximum=numbers_list[0]            #minimum=numbers_list[0]
for value in numbers_list:
    if(value>maximum):             #if(value<minimum)
        maximum=value              #minimum=value
print(maximum) 