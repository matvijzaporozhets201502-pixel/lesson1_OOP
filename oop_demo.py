
class Student:
    amount_of_students = 0

    def __init__(self, name, height):
        self.name = name
        self.height = height
        Student.amount_of_students += 1

    def grow(self, cm):
        self.height += cm

bob = Student('Bob', 150)
kate = Student('Kate', 155)
Student.amount_of_students += 1

print(bob.name, bob.height,)
print(kate.name, kate.height)
bob.grow(11)
print(bob.name, bob.height)