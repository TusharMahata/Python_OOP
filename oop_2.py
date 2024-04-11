# Creating a class

class Dog:

    def __init__(self, name):
        self.name = name
        #print(self.name)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

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
print(d1.name)
print(d1.get_name())
d1.set_name('Tim')
print(d1.get_name())

dogs_name = ['Mona', 'Tiger', 'Harry']
dogs = Dog(dogs_name)
print(dogs.get_name())