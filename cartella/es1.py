
def sum_list(lista):
    if lista == None:
        return None
    else:
        result = 0
        for item in lista:
            result=result+item
        return result

lista = []
test=sum_list(lista)
print('risultato: {}'.format(test))