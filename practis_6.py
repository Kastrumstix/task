class Human:
    def __init__(self, name):
        self.name = name



class Student(Human):
    def __init__(self, name, place):
        Human.__init__(self, name)
        self.name = name



human = Human('Михаил')
print(human.name)
student = Student('Vfrc', 'urban')
print(student.name)
