class Student:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.grade = {"chinese" : 0,"english" : 0,"math" : 0}
    def set_grade(self,course,grade):
        if course in self.grade:
            self.grade[course] = grade
    def print_grade(self):
        print(f"student: {self.name}(number:{self.number})")
        for course in self.grade:
            print(f"{course}:         {self.grade[course]}")

mike = Student("Mike",2025031001020)
mike.set_grade("math",150)
mike.print_grade()
