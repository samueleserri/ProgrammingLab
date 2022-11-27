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
        result = []
        lista=super().get_data()
        for element in lista:
            try:
               result = float(element[1])
            except Exception as e:
                if len(element[1])==0:
                    print('Errore, non ci sono valori')
            except ValueError:
                if element[1] == 'ciao':
                    print('Errore non posso convertire "Ciao" a nuemro')
        return result            
            
        
        
        
        
    
    

#csvfile=NumericalCSVFile('shampo_sales.csv')
#data=csvfile.get_data()
#print(data)
