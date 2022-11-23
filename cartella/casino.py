import random

class Dadi():
    def __init__(self, faccie):
        
        self.faccie=faccie
        
    def tiro(self):
        number=self.faccie
        esito = random.randint(1, number)
             
        return esito


numero=input('inserisci il numero di faccie:_')
numero=float(numero)
if numero==0:
    print('inserisci un numero > di 0')
else:    
    dado=Dadi(numero)
    d=dado.tiro()
    
    guess=input('prova a indovinare:_')
    guess=float(guess)
    
    if(d==guess):
        print('you win')
        
    else:
        print ('you lose')
    print('è uscito', d)   