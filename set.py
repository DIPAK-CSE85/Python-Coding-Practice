set={'dipak',34,34.56,True,12,12,34,34,12}
print(set)
print(len(set))
set1={"dipak","suraj","rohit"}
set1.add(90)
set1.pop()
#set1.remove(90)
set1.discard(100)    # its remove number only if the number is present othewise its only execute
set1.add((100,400,500))  #tuple io added because it is immutable
#set.add([234,678,654])   #list not added because it is mutable
print(set1)
