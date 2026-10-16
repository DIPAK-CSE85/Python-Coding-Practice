class complexNumber:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,other):
      return  f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
s1=complexNumber(1,2)
s2=complexNumber(5,6)  
print(s1+s2)   ##compair the object


class billpay:
   def __init__(self,name,age):
      self.name=name
      self.age=age
   def __gt__(self,x):
      if self.age>x.age:
         return True
      else:
         return False  
b1=billpay(input("enter your name:"),int(input("enter your age:")))
b2=billpay(input("enter your friend name:"),int(input("enter your friend age:")))
if b1>b2:    #compair the object
   print(f"{b1.name} will pay the bill")
else:
   print(f"{b2.name} will pay the bill")     

