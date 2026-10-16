list1=[1,1,1]
list2=[1,1,1]
list3=[1,1,1]
print(f"{list1}\n{list2}\n{list3}")
matrix=[list1,list2,list3]
print(matrix)
position=input("enter the position where you want to hide money=")
row_num=int(position[0])
coloum_num=int(position[1])
matrix[row_num-1][coloum_num-1]='x'
print(f"{list1}\n{list2}\n{list3}")