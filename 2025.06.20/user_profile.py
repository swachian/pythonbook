def build_profile(first_name, last_name, **kwargs):
    kwargs['first_name'] = first_name
    kwargs['last_name'] = last_name
    return kwargs

my_profile = build_profile("Jian", "You", height = 1.73, weight = 88, sex = 'Male')
print(my_profile)

class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.sex} and at the age of {self.age}")
    
    def greet_user(self):
        print(f"Welcome {self.first_name}")

user1 = User("qin", "hui", 72, 'male')
user2 = User("zhao", "hui", 62, 'female')

user1.describe_user()
user2.describe_user()
user2.greet_user()


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):

    def __init__(self, first_name, last_name, age, sex, privileges):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()


admin = Admin('dd', "zz", 18, 'male', ["can add post", "can delete post", "can ban user"])
admin.show_privileges()