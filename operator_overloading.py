class p:
    def __init__(self,p):
        self.a=p
    def __add__(self,other):
        return self.a + other.a
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
wow=p(23)
pet=p(30)
print(pet>wow)