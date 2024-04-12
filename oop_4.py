# Inheritence
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'my name is: {self.name}, age: {self.age}')
fav = Pet('Luffi', 2)
fav.info()

class Dog(Pet):
    def speak(self):
        print('Ghew')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print(f'I am {self.name}, age: {self.age}, color: {self.color}')
pet_dog = Dog('Luffi', 1)
pet_dog.info()
pet_dog.speak()

pet_cat = Cat('Oggy', 2, 'white')
pet_cat.speak()



