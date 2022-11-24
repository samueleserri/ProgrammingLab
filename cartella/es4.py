class CSVfile():
    def __init__(self, name):
        self.name=name

        def get_data(self):
            values = []
            
            my_file=open(self.name, 'r')
        
            for line in my_file:
                elements=line.split(',')
                if elements[0]!='Date':
                    value=elements[1]
                    values.append(float(value))
            my_file.close()

            list = []
            for item in values:
                list.append(item)

            return list

    