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
            n_colonne=len(item)
        lunghezza_file=len(lista)    
        for element in lista:
            for i in range(n_colonne):
                if i > 0:
                    try:
                        result.append(float(element[i]))
                    except ValueError:
                        print('Error')
                    except Exception as e:
                        print('Error')
               


        return result          
            
        
        
        

#csvfile=NumericalCSVFile('shampo_sales.csv')
#data=csvfile.get_data()
#print(data)
