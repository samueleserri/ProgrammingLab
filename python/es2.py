from math import e, pow, pi
import math

class Funzione():   
#super classe che rappresenta una generica f(x)
        
    def eval(self,x): 
        pass
#metodo che aprossima il valore di un integralle definito in un intervalo [a, b]
    def calcola_integrale(self, a, b, m):
        h = (b-a)/m
        return h * sum([self.eval(a+i*h) for i in range(m)])
            
#sottoclassw ch erappresenta una funzione spacifia
class Funzione1(Funzione):
#vado adefinire il metodo ch edefinisce la legge di trasformazione della funzione
        def eval(self, x):
            return x**2-2*x

#instanzio un oggetto nella sua specifica classe
parabola=Funzione1()
#chiamo il metodo che calcola l'integrale definito nella superclasse per l'istanza dello specifico ogetto parabola
integrale_parabola=parabola.calcola_integrale(0, 1, 250)
        
class Funzione2(Funzione):
        
        def eval(self, x):
            return pow(e, 2*x)

Funzione2=Funzione2()
result = Funzione2.calcola_integrale(pi, -pi/2, 100)
print(result)
class Funzione3(Funzione):
        def eval(self, x):
            return x/(1+x**2) 

funzione3=Funzione3()
funzione3_integrale=funzione3.calcola_integrale(-2, 2, 1000)
print(funzione3_integrale)

class Funzione4(Funzione):    

    def eval(self, x):
        return math.log(x, e)

funzione4=Funzione4()
logaritmo_integrale = funzione4.calcola_integrale(1, 3, 1000)
print(logaritmo_integrale)