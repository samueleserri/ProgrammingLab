class Rettangolo:
    def __init__(self, base, lunghezza):
        self.base=base
        self.lunghezza=lunghezza
    def area(self):
        return self.base*self.lunghezza


class Parallelepipedo(Rettangolo):
    def __init__(self, base, lunghezza, altezza):
        super().__init__(base, lunghezza)
        self.altezza=altezza
    def Volume(self):
        return (super().area()*self.altezza)
        

parallelpipedo=Parallelepipedo(5,5,5)
print(parallelpipedo.Volume())
print(parallelpipedo.area())
    