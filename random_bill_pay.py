import random
name=input("enter everybody names seperated by comma=")
name_list=name.split(",")
print(name_list)
length=len(name_list)
r=random.randint(0,length-1)
print(f"{name_list[r]} will pay the bill")



import random
name=input("enter everybody names seperated by comma=")
name_list=name.split(",")
print(name_list)
choice=random.choice(name_list)
print(f"{choice} will pay the bill")