class Person():

    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
    def say_hy(self):
        print('Hello i am "{}" "{}"'.format(self.name, self.surname))

class Student(Person):
   
    def say_hy(self):
        print('Hello i am  Student "{}" "{}"'.format(self.name, self.surname))

