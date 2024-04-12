# class_method
class Person:
    number_of_person = 6

    def __init__(self, name):
        self.name = name
        Person.add_people()

    @classmethod
    def people_count(cls):
        return cls.number_of_person
    
    @classmethod
    def add_people(cls):
        cls.number_of_person += 1

p = Person('Tushar')
print(p.name)
print(p.number_of_person)
print(Person.number_of_person)
# print(Person.name) Here need to create class instance
print(Person.people_count())