num1={12,43,56,78}
num={1,2,3}
num2={87,45,43,89,56,12,78}
# disjoint
print(num1.isdisjoint(num2))  # it return true if all element of set1 is different from set2 otherwwise false
print(num.isdisjoint(num1)) 
# subset 
print(num1.issubset(num2))  #it return true if all elements of set1 is in set2 otherwise false
print(num.issubset(num1))
print(num1 <= num2)   # using operator
#superset
print(num2.issuperset(num1))   ##it return true if set2 contains all elements of set1 otherwise false
print(num1.issuperset(num2))
print(num2 >= num1)   # using operator

num3={1,2,3}
del num3      #it removes all elements as well complete set (error is print)
print(num3)