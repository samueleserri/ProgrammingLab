class Person():
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname

    def __str__(self):
        return 'Person "{}" "{}"'.format(self.name, self.surname)
    
    def lista(self):
        incidente=[]
        incidente.append(self.name)
        incidente.append(self.surname)
        
        
        

person = Person('Beppe', 'Grillo')
print(person)
print(person.name)
print(person.surname)
person.lista()