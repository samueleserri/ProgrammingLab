class Function:
    def __init__(self, name, a, b):
        self.name=name
        self.a=a
        self.b=b
        
    def min_value(self, delta_x=0.5):
        x_start=self.a
        x_end=self.b
        i=0
        f_x=[]
        abs_f_x=[]
        x = []
        while(x_start+i*delta_x)< x_end:
            this_x=x_start+i*delta_x
            this_fx=self.eval(this_x)
            x = x+[this_x]
            f_x = f_x +[this_fx]
            abs_f_x=abs_f_x+[abs(this_fx)]
            i=i+1

        min = 0
        for i in  range(1, len(abs_f_x)):
            if abs_f_x[i]<abs_f_x[min]:
                min=i

        return min
    
    def eval(self, x):
        pass
        

class Parabola(Function):
    def eval(self, x):
        return x

parabola=Parabola('parabola', -10, 10)
print(parabola.min_value())