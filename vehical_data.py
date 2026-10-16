from abc import ABC,abstractmethod
class vehical:
    def __init__(self,n):
        self.num_of_tyers=n
    @abstractmethod    
    def start(self):         #Abstracts method
        pass
    def display(self):         #concrint method
        print("Your vehical is very clean")