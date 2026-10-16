def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x//y
def calculate(m):       #pass a function as a argument 
    ans=m(12,6)
    print(f"answer is={ans}")
calculate(div)    



def upper_name(name):
    return f"name is:{name.upper()}"
def lower_name(name):
    return f"name is:{name.lower()}"
print(upper_name("dipak"))
print(lower_name("PRANAY"))




def add(x,y):
    return x+y

addition=add
print(addition(12,13))