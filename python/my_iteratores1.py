class MyPower:
    def __init__(self,a):
        self.a=a
        self.current = 0
    def __iter__(self):
        print(self.current)
        return self
    def __next__(self):
        if self.current>self.a:
            raise StopIteration 
        self.current+=1
        return (3**self.current)/self.current
    def mean_pow(self):
        self.current=0
        list = [self.__next__() for i in range(self.a)]
        return sum(list)/len(list)

class Polinomi:
    def eval(self):
        pass

class obs1(Polinomi):
    def __init__(self, x ):
        self.x=x
    def eval(self):
        return self.x**2+2*self.x
class obj2(Polinomi):
    def __init__(self, x ):
        self.x=x

    def eval(self):
        return self.x**2+2*self.x-1
    