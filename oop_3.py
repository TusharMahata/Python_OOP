class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.garde = grade

    def get_garde(self):
        return self.garde
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        # here every student is a class. 
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_garde()
        return value / len(self.students)

stu_one = Student('Porimoni', 30, 25)
stu_two = Student('Shawon', 26, 22)
stu_three = Student('Tushar', 27, 21)

course = Course('Math', 2)
course.add_student(stu_one) # an intence Student class is passed in Course class. 
course.add_student(stu_two)
course.add_student(stu_three) # Not able to take input


print(course.name)
print(course.students)
print(course.students[0].name)
print(course.get_average_grade())