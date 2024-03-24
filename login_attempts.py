class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User {self.first_name} {self.last_name} is from {self.location} and is {self.age}.")
       
    def greet_user(self):
        print(f"\nWelcome back, {self.first_name} {self.last_name}.\n")

    def read_login_attempts(self):
        print(f"You have attempted to login {self.login_attempts} time(s).")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user_one = User('Alicia', 'Gull', 24, 'Arden')

user_one.describe_user()
user_one.greet_user()
user_one.increment_login_attempts(1)
user_one.increment_login_attempts(1)
user_one.increment_login_attempts(1)
user_one.read_login_attempts()
user_one.reset_login_attempts()
user_one.read_login_attempts()