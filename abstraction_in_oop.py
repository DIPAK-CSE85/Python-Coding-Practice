from vehical_data import vehical
class Bick(vehical):
    def __init__(self,n,colour):
        super().__init__(n)
        self.colour=colour
    def start(self):
        print("start by kick")
class schooti(vehical):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("self started")
class car(vehical):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("start by key")
class truck(vehical):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("start by self")                        
