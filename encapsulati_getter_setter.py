class student:
    def __init__(self,name,roll,age):
        self.name=name       #public instance variable
        self._roll=roll       #protect instance variable
        self.__age=age        #private instance variable
    def __display(self):
        print(f"My name is {self.name}, my roll number is {self._roll} and my age is {self.__age}")    
    def get_a(self):
        return self.__age
    def set_AGE(self,new_age):
        if new_age>25:
            print("your age is invalid")
        else:    
            self.__age=new_age    
s=student("Dipak",16,21)
print(s.name)
print(s.get_a())
s.set_AGE(24)
print(s.get_a())
