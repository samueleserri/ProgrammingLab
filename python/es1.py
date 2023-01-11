import math
class Figure():
    def perimetro(self):
        pass
    def area(self):
        pass

class Triangolo(Figure):
    def __init__(self, lato1, lato2,lato3):
        self.lato1=lato1
        self.lato2=lato2
        self.lato3=lato3
        
        if self.lato1==self.lato2 and self.lato2==self.lato3:
            print('triangolo equilatero')
        elif self.lato1 != self.lato2 and self.lato2 != self.lato3 and self.lato1 != self.lato3:
            print('scaleno')
        else:
            print('isoscele')
    def perimetro(self):
        perimetro = self.lato1+self.lato2+self.lato3
        print(perimetro)
    def area(self):
        p=(self.lato1+self.lato2+self.lato3)/2
        area = math.sqr(p*(p-self.lato1))
        print(area)

        
        
class Rettangolo(Figure):
    def __init__(self, lato1, lato2):
        self.lato1=lato1
        self.lato2=lato2
        if self.lato1==self.lato2:
            print('quadrato')
        else:
            print('non quadrato')

        def perimetro(self):
            perimetro = (lato1+lato2)*2
            print(perimetro)
        def area():
            area = self.lato1*self.lato2
            print(area)

class Cerchio(Figure):
    

    def __init__(self, raggio):
        self.raggio=raggio

    def perimetro(self):
        pi = math.pi
        perimetro = 2*self.raggio*pi
        print(perimetro)

    def area(self):
        pi = math.pi
        area = (self.raggio**2)*pi
        print(area)
    
rettangolo=Rettangolo(5,5)
print(rettangolo.perimetro())

        