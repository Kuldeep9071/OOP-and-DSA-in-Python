# Object Oriented Programming Python

class User:
    # Constructor in Python
    def __init__(self,username,name,email):
        self.name=name
        self.username=username
        self.email=email
        print(f"New user created with name {name}")

    # We can create as many function as we want for eg
    # Also Know as "Method"

    def Introduction(self,guest_name):
        print(f"Hi {guest_name}, I am {self.name} You can contact me at {self.email}")

user1=User("abc123","abc","abc@email.com")
user2=User("xyz123","xyz","xyz@email.com")
print(user1.name)

user1.Introduction("Jhon")




