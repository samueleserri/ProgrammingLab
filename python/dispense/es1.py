lista= [x**3 for x in range(10)]

class Pow3:
    def __init__(self, x):
        self.max=x
    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<=self.max:
            result=3**self.n
            self.n+=1
            return result
        else:
            raise Exception('stop iteration')
            
x=609    
numbers = Pow3(x)
i = iter(numbers)
for j in  range(x):
    print(next(i))