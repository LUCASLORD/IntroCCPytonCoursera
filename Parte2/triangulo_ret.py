import math

class Triangulo:

    def __init__(self, a,b,c):
    
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        '''Teorema de pitágoras quadrado da hipotena
        = soma dos quadrados dos catetos h² = c² + c²'''
        if self.a > self.b and self.a > self.c:
            if (self.a * self.a)  == ( (self.b * self.b) +(self.c * self.c) ):
                return True
            else:
                return False
        elif self.b > self.a and self.b > self.c:
            if (self.b * self.b) == ((self.a * self.a) + (self.c * self.c) ):
                return True
            else:
                return False
        elif self.c > self.a and self.c > self.b:
            if (self.c * self.c) == ( ( self.a * self.a) + (self.b * self.b) ):
                return True
            else:
                return False
        else:
            return False



