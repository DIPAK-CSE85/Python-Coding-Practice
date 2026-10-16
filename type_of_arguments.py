#position
def add(name,mark):
    print("name is=",name)
    print("marks are=",mark)
add(49,"dipak")    

#keyword
def add(name,mark):
    print("name is=",name)
    print("marks are=",mark)
add(mark=49,name="dipak")    


#mixed
def add(a,name,mark):       #first position and then keyword
    print("name is=",name)
    print("marks are=",mark)
    print(a)
add(123,mark=49,name="dipak")     #first position and then keyword

#default
def add(name,mark,dept="CSE"):      #dept is a default argument 
    print("name is=",name)
    print("marks are=",mark)
    print("deperament=",dept)
add(mark=49,name="dipak") 
add(mark=49,name="dipak",dept="AI")


#orbitory argument
#position orbitory argument
def add(*numbers):
    sum=0
    for i in numbers:
       sum+=i
    print("sum is" \
    "",sum)
add(1,2,4,)
add(12,13,143,14,)
add(1,2,3,4,5,6,7)      

#position orbitory argument
def pro(*numbers):
    pro=1
    for i in numbers:
       pro*=i
    print("pro is",pro)
pro(1,2,4,)
pro(12,13,143,14,)
pro(1,2,3,4,5,6,7)


#keyword
def info(**names):
    for key,value in names.items():
        print(key,value)   
info(name1="dipak",name2="suraj",name3="rohit",name5="ketan",name4="pranay") 
info(name3="rohit",name5="ketan",name4="pranay")
info(name3="rohit",name4="pranay")


def info(*num,**names):
    for key,value in names.items():
        print(key,value)
    print(num)    
info(name1="dipak",name2="suraj",name3="rohit",name5="ketan",name4="pranay") 
info(name3="rohit",name5="ketan",name4="pranay")
info(1,2,3,name3="rohit",name4="pranay")