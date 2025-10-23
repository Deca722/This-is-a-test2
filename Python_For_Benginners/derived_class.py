class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2
    def breath(self):
        print(self.name +" breathing")
    def poop(self):
        print(self.name +" pooping")
class Dog(Mammal):
    def __init__(self,name,sex):
        super().__init__(name,sex)
        self.has_tail = True
    def scratch_sofa(self):
        print(self.name +" scratch sofa")

class Emploee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_into(self):
        print(f"name: {self.name} (id: {self.id})")


class FullTimeEmploee(Emploee):
    def __init__(self,name,id,month_salary):
        super().__init__(name,id)
        self.month_salary = month_salary
    def calculate_salary(self):
        print(f"{self.name} salary: {self.month_salary}")


class PartTimeEmploee(Emploee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calculate_salary(self):
        result =  self.work_days * self.daily_salary
        print(f"{self.name} salary:  {result}")


mike = PartTimeEmploee("Mike",1,100,10)
mike.print_into()
mike.calculate_salary()