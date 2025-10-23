class CuteCat:
    def __init__(self,cat_name,cat_age):
        self.name = cat_name
        self.age = cat_age
    def speak(self):
        print("miao~ " * self.age)
    def say(self,content):
        print(f"cat {self.name} says {content}.")
cat_my = CuteCat("Peter",4)
print(f"my cat is {cat_my.name}!")
cat_my.speak()
cat_my.say("hahaha")
