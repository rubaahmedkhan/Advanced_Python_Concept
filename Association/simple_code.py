class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching...")

class Student:
    def __init__(self, name):
        self.name = name

    def attend_class(self, teacher):
        print(f"{self.name} is attending class of {teacher.name}")
        teacher.teach()

# Creating objects
t1 = Teacher("Sir Ali")
s1 = Student("Ruba")

# Association: Student uses Teacher
s1.attend_class(t1)


# output
# Ruba is attending class of Sir Ali
# Sir Ali is teaching...
