# Creating a class

class Dog:

    def add_dog(self, x):
        return x + 1

    def bark(self):
        print('ghew')


d = Dog()
d.bark()
print(d.bark()) # this print returns with ghew and none
print(d.add_dog(7))