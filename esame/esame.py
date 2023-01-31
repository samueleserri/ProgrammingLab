class ExamException(Exception):
        pass

class CSVFile:

    def __init__(self, name):
            self.name = name

    
    def get_data(self):
        values = []
        try:
            #provo ad aprire il file
            my_file=open(self.name, 'r')
        except:
            print('Errore, inserire un file')
        try:
            #verifico che il file sia leggibile
            my_file.readline()
        except:
            raise ExamException('file illegibile')
        if my_file == []:
            return None       
        for line in my_file:
            elements=line.strip('\n').split(',')
            if elements[0]!='epoch':
                values.append(elements)   
        my_file.close()
        #return di una lista di liste in cui i valori sono formato stringa
        return values

class CSVTimeSeriesFile(CSVFile):
    
    
    def get_data(self):
        lista=super().get_data()
        result = []
        for item in lista:
            lista_numerica=[]
            for i, element in enumerate(item):
                if i == 0:
                    try:
                    #converto a int i valori epoch
                        lista_numerica.append(int(element))
                    except:
                    #se c'è un elemento che non può essere convertito vado avanti
                        continue
                else:
                ##converto a float le temperature
                    try:
                        lista_numerica.append(float(element))
                    except:
                    #vado avanti se non possono esere convertiti
                        continue
                if len(lista_numerica)==len(item):
                    result.append(lista_numerica)
        #return di una lista di liste con i valori convertiti
        return result   

    
    

def liste_giornaliere(time_series):
    #questa lista contiene altre liste che contengono le temperature relative ad un singolo giorno
    lista = []
    #lista di supporto su cui memorizzo le temperature di un giorno nel for
    day = []
    first_element = time_series[0]
    #inizializzo una variabile con il primo epoch
    curr_day = first_element[0]
    for element in time_series:
        #aggiungo a day fino a che le temperature sono relative allo stesso giorno
        if start_day(element[0]) == curr_day:
            day.append(element[1])
        else:
            #quando si passa a un giorno successsivo aggiungo la lista day alla lista, resetto il contenuto di day e incremento il giorno corrente
            lista.append(day)
            day = []
            curr_day+=86400
    #aggiungo i valori dell'ultimo giorno
    lista.append(day)
            
    
    return lista

 

            
    
            
    

    

def compute_daily_max_difference(time_series):
    listegiornaliere = liste_giornaliere(time_series)
    return [abs(max(listegiornaliere[i])-min(listegiornaliere[i])) for i in range(len(listegiornaliere))]



def start_day(epoch):
    return epoch - (epoch % 86400)  


#_______________TEST_______________________________#
def test_start_day():
    if start_day(1553932800) != 1553904000:
        raise ExamException('errore nel calcolo inizio del giorno')


    
    


test=CSVTimeSeriesFile('data.csv')
time_series = test.get_data()
#print(time_series)
print(compute_daily_max_difference(time_series))
test_start_day()


