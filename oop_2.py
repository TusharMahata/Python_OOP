# Creating a class

class Dog:

    def __init__(self, name):
        self.name = name
        print(self.name)

    def add_dog(self, x):
        return x + 1

    def bark(self):
        print('ghew')


#d = Dog() #missing requirment Argumant
#d.bark()
#print(d.bark()) # this print returns with ghew and none
#print(d.add_dog(7))
d1 = Dog('Luffi')
#print(d1)