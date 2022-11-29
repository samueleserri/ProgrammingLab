class CSVFile():
    
    def __init__(self, name):
        self.name=name

    def get_data(self):
        values = []
        try:
            my_file=open(self.name, 'r')
        except:
            print('Errore, inserire un file')
        if my_file == []:
            return None       
        for line in my_file:
            elements=line.strip('\n').split(',')
            if elements[0]!='Date':
                values.append(elements)   
        my_file.close()
        return values    

class NumericalCSVFile(CSVFile):

    def get_data(self):
        lista=super().get_data()
        result = []
        for item in lista:
            lista_numerica=[]
            for i, element in enumerate(item):
                if i ==0:
                    lista_numerica.append(element)
                else:
                    try:
                        lista_numerica.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
            if len(lista_numerica)==len(item):
                result.append(lista_numerica)
        return result          
            
        
        
        

csvfile=NumericalCSVFile('shampo_sales.csv')
data=csvfile.get_data()
print(data)