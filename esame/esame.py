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
            ExamException('Errore, inserire un file')
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

    def __init__(self, name):
        super().__init__(name)
    
    
    def get_data(self):
        lista=super().get_data()
        result = []
    
        for item in lista:
            lista_numerica = []
            for i,element in enumerate(item):
                if i == 0:
                    try:
                        lista_numerica.append(int(element))
                    except:
                        continue
                else:
                    try:
                        lista_numerica.append(float(element))
                    except:
                        continue
                if len(lista_numerica) == 2:
                    result.append(lista_numerica)
        #return di una lista di liste con i valori convertiti
        check_list(result)
        return result  

    
def check_list(list):
    last_day = 0 
    for item in list:
        if last_day >= item[0]:
            raise ExamException('lista non ordinata o duplicato')
        last_day = item[0]

def liste_giornaliere(time_series):
    #questa lista contiene altre liste che contengono le temperature relative ad un singolo giorno
    result = []
    #lista di supporto su cui memorizzo le temperature di un giorno nel for
    day = []
    first_element = time_series[0]
    #inizializzo una variabile con la mezzanotte del primo giorno
    curr_day = start_day(first_element[0])
    
    for element in time_series:
        #aggiungo a day fino a che le temperature sono relative allo stesso giorno
        if start_day(element[0]) == curr_day:
            day.append(element[1])
        else:
            #quando si passa a un giorno successsivo aggiungo la lista day alla lista, resetto il contenuto di day e incremento il giorno corrente
            if day != []:
                result.append(day)
            day = []
            curr_day+=86400
    #aggiungo i valori dell'ultimo giorno
    if day != []:
        result.append(day)     
    return result
    
def compute_daily_max_difference(time_series):
    #se si passa qualcosa che è diverso da una lista alzo un eccezione
    if type(time_series) != list:
        raise ExamException('compute_daily_max_difference prende in input una lista')
    if time_series == []:
       raise ExamException('lista vuota')
    listegiornaliere = liste_giornaliere(time_series)
    
    escursioni_termiche = []
    for item in listegiornaliere:
        if len(item) <= 1:
            escursioni_termiche.append(None)
        else:
            escursioni_termiche.append(abs(max(item)-min(item)))
    return escursioni_termiche
    
def start_day(epoch):
    return epoch - (epoch % 86400) 