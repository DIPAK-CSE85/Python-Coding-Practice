#identity operator work on the address of the data not on the data.
a=10
b=10
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

#equality operator work on data not on address
print(a==b)