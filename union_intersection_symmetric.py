set={"dipak","rohit","ketan","suraj"}
set1={"mandar","bhushan","dipak","rohit"}
set2={"pranay","sahil","jaivik","dipak"}
#print(set.union(set1))
#print(set.union(set1,set2))
#print(set.union(("anshu","prem")))  #tuple also possible
print(set.union(["anshu","prem"]))  #list also possible
#print(set1|set2)
#print(set1|set2|set)
#set.update(set2)    #add data of set2 into set
#set.update([23,44,67])   # also possible
set|=set2   #also possible
print(set)