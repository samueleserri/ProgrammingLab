from math import pow, e

class Function:
#"function R -> R"
    def eval(self):
        pass
    def valore_medio(self, a, b, N):
        sigma=(b-a)/N
        sum = 0
        for i in range(N):
            sum = sum + self.eval(a+i*sigma)
        return (1/N)*sum


class Funzione1(Function):
    def eval(self, x):
        return 2*pow(x, 2)+2*x

parabola=Funzione1()
result=parabola.valore_medio(0, 6, 3)
print(result)

class Exp(Function):
    def eval(self, x):
        return pow(e, x)

exp=Exp()
print(exp.valore_medio(1,50,1))
    


def test_valore_medio():
    class identità(Function):
        def eval(self, x):
            return x
    bisettrcie=identità()
    result = bisettrcie.valore_medio(1,3,2)
    if result != 0.5*(3.0):
        raise Exception('Errore nel metodo: valore_medio')

test_valore_medio()       

