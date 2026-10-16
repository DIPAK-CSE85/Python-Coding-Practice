def bubble(list,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                print(f"{j}to{j+1}")
        print(list)            
list=[4,1,5,3,2]
n=len(list)
bubble(list,n)