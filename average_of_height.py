height=(input("enter a height of everybody seperated by comma="))
height_list=height.split(",")
print("list in string form",height_list)
count=0
sum=0
for x in height_list:
    count=count+1
print("lingth of list is",count)
for i in range(0,count):
    height_list[i]=int(height_list[i])
    sum=sum+height_list[i]
average=sum//count
print("list in integer form",height_list)
print("total sum is=",sum)
print("average height is=",average)
