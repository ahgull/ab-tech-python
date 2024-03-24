class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    def describe_user(self):
        print(f"User {self.first_name} {self.last_name} is from {self.location} and is {self.age}.")
    def greet_user(self):
        print(f"\nWelcome back, {self.first_name} {self.last_name}.\n")

user_one = User('Alicia', 'Gull', 24, 'Arden')
user_two = User('Preston', 'Gull', 26, 'Arden')

user_one.describe_user()
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()