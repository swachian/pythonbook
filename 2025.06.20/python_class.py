class Dog:
    """A dog class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")  
    
    def roll_over(self):
        print(f"{self.name} rolled over") 

dog = Dog('aaa', 5)
dog.roll_over()
print(f"dogs is at {dog.age} old")