class Model():
    def fit(Self, data):
        raise NotImplementedError('metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('metodo non implementato')

class IncrementModel(Model):
    def predict (self, data):
        if not  check_input(data):  #controllo che data sia una lista
            raise Exception('Errore, oggetto non è una lista')
            return None
        numero_elementi = len(data) #conto il numero di elementi della lista
        if numero_elementi==1:
            raise Exception()  #se c'è un solo elemento alzo un eccezione perchè non c'è nessun incremeno da calcolare
            return None
        numero_elementi=numero_elementi-1  #la divisione va fatta per n_elementi -1
        incremento_medio = 0  #variabile che contiene l'incremento medio
        prev_values = None    #variabile che tien etraccia dell'elemento precedente, inizializata a None perchè il primo elemento non ha nessun precedente
        for item in data:     #ciclo tutti gli eloementi della lista
            if prev_values != None:   #se non sono al primo elemento
                    incremento_medio=incremento_medio + (item - prev_values) #incremento medio è uguale a se stesso più la differenza tra il numeor attuale e quello precedente nella lista
            prev_values = item #aggiorno il precedente

        incremento_medio = incremento_medio/(numero_elementi)  #per definizione l'incremento medio si calocla così
        predict = data[-1]+incremento_medio  #data[-1] mi permette di accedere all'ultimo elemento della lista
        
        return predict  #return del valore finale

def check_input(lista):
    if type(lista) != list:
        return False
    else:
        return True