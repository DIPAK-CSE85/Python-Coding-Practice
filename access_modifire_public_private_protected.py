class student:
    def __init__(self,name,roll,age):
        self._name=name    #protected instance varible
        self.roll=roll     #public instance varible
        self.__age=age     #private instance varible 
    def work(self):
        print("I can work")
    def __data(self):
        print(f"My name is {self._name}  and roll number is {self.roll} my age is {self.__age}")       
class sub(student):
    def __init__(self,name,roll,age):
        super().__init__(name,roll,age)
    def display(self):
        print(f"My name is {self._name}  and roll number is {self.roll} my age is {self.__age}")    
s=sub("dipak",16,20)
print(s._name) 
print(s.roll)    
print(dir(s))     # not access
s.work()      
#s.display()
s._student__data()