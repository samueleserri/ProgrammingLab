class MovingAverage:
    def __init__(self, dim):
        if type(dim)==float:
            raise ExamException('idk')
        try:
            dim=int(dim)
        except:
            raise ExamException('conversione a int fallita')

        if dim <= 0:
            raise ExamException('Errore, finestra nulla o minore di zero')
        self.dim=dim


    def somme_parziali(self, valori, n):
        return [sum(valori[i:i+n]) for i in range(len(valori)-n+1)]
    
    def compute(self, lista):
        if type(lista) != list:
            raise ExamException('lista non trovata')
        if lista == [] or lista == None:
            raise ExamException('Errore lista vuota')
        for element in lista:
            try:
                element=float(element)
            except:
                raise ExamException('conversione a float fallita')
        if len(lista)<self.dim:
            raise ExamException('la finestra è più grande della lista')
        x = self.somme_parziali(lista, self.dim)
        print(x)
        return [x[i]/self.dim for i in range(len(x))]


class ExamException(Exception):
    pass


def test():
    if MovingAverage(-2) != ExamException:
        raise ExamException('Errore nel test di validità della finestra')
    test_eccezioni = MovingAverage(2)
    if test_eccezioni.compute([]) != ExamException:
        raise ExamException('errore nel test di validità della lista')

def test_correttezza():
    test=MovingAverage(2)
    if test.compute([2,4,8,16]) != [3.0, 6.0, 12.0]:
        raise ExamException('errore nel metodo compute')
