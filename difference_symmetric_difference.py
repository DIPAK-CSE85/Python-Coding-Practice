set1={"dipak","suraj","rohit"}
set2={"dipak","ketan","mandar"}
set3={"dipak","sahil","jaivik","rohit"}
   #difference
#print(set1.difference(set2))
#print(set2.difference(set1))
#print(set1.difference(set2,set3))
#print(set3.difference(set1,set2))
#set1.difference_update(set2)
#set1.difference_update(("dipak","prem"))
#print(set1)


    #symmetic difference
#print(set1.symmetric_difference(set2))
#print(set2.symmetric_difference(set1))
#print(set1.symmetric_difference(set3))
#print(set3.symmetric_difference(set1))
#set1.symmetric_difference_update(set2)
set1.symmetric_difference_update(("dipak","prem"))
print(set1)