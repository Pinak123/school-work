class p:
    def __init__(self,p,q):
        self.a=p
        self.b=q
    def __add__(self,other):
        return self.a + other.a , self.b  + other.b
    def __sub__(self,other):
        return self.a - other.a
    def __mul__(self,other):
        return self.a * other.a
    def __gt__(self,other):
        return self.a > other.a
    def __lt__(self,other):
        return self.a < other.a
    def __ne__(self,other):
        return self.a != other.a
    def __truediv__(self,other):
        return self.a / other.a
    def __floordiv__(self,other):
        return self.a // other.a
wow=p(23,100)
pet=p(30,233)
print(pet+wow)