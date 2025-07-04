class Department:
    def __init__(self, name):
        self.name = name

class Professor:
    def __init__(self, name, dept):
        self.name = name
        self.department = dept   # Association with Department

    def details(self):
        print(f"Professor: {self.name} | Department: {self.department.name}")

# Create Department
cs_dept = Department("Computer Science")

# Associate Professor with Department
prof1 = Professor("Dr. Zahid", cs_dept)
prof1.details()


# 0utput
# Professor: Dr. Zahid | Department: Computer Science