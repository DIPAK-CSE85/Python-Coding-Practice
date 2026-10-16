#first
class instruction:
    mark=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def change(self,roll_no): 
         print(f"my name is {self.name},and my roll number is {roll_no}")
         self.mark+=1  
    def update(self,number):
        print(f"my mobile number is={number} {self.name}")  
        self.mark+=1     
data=instruction("dipak","lawadi")
print(data.name)
print(data.address)
data.change(16)
print(data.mark)
data.update(9637671522)
print(data.mark)
data_2=instruction("pranay","pauni")
print(data_2.name)
print(data_2.address)
data_2.change(234)
print(data_2.mark)
data_2.update(8482997668)
print(data_2.mark)