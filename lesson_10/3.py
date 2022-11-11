class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_P(self):
        P = self.a + self.b + self.c
        return P

    def get_S(self):
        P = self.get_P() / 2        
        S = (P * (P - self.a) * (P - self.b) * (P - self.c))**0.5
        return S


    
t1 = Triangle(2, 2, 3)

print(t1.get_P())
print(t1.get_S())