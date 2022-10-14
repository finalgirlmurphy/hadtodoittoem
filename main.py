#9.1
class Restaurant() :
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        msg = (f"{self.name} serves {self.cuisine_type}.")

        print(msg)
    def open_restaurant(self):
        msg = self.name + " is open and ready to serve!"
        print(msg)

restaurant = Restaurant('Olive Garden', 'lasagne')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2
class Restaurant() :
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        msg = (f"{self.name} serves {self.cuisine_type}.")

        print(msg)
    def open_restaurant(self):
        msg = self.name + " is open and ready to serve!"
        print(msg)

restaurant = Restaurant('Olive Garden', 'lasagne')
restaurant.describe_restaurant()
dominos = Restaurant('Dominos', 'pizza')
dominos.describe_restaurant()
jj = Restaurant('Jimmy Johns', 'subs')
jj.describe_restaurant()

#9.3
class User():

    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.age = age.title()
        self.location = location.title()

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Age: " + self.age)
        print("Location: " + self.location)

    def greet_user(self):
        print("\nGood afternoon, " + self.username + "!")
betty = User('betty', 'smith', 'beesmith', '30', 'United States')
betty.describe_user()
betty.greet_user()
sam = User('sam', 'mcdonald', 'burgerboy', '25', 'Africa')
sam.describe_user()
sam.greet_user()

#9.4
class Restaurant() :
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        msg = (f"{self.name} serves {self.cuisine_type}.")
        print(msg)
    def open_restaurant(self):
        msg = self.name + " is open and ready to serve!"
        print(msg)
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, all_served):
        self.number_served += all_served

restaurant = Restaurant('panera', 'broccoli soup')
restaurant.describe_restaurant()

print("\nHow many people served: " + str(restaurant.set_number_served))

restaurant.number_served = 200
print("How many people served: " + str(restaurant.number_served))

restaurant.set_number_served(500)
print("How many people served: " + str(restaurant.number_served))

restaurant.increment_number_served(350)
print("How many people served: " + str(restaurant.number_served))

#9.5
class User():

    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.age = age.title()
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Usernameis " + self.username)
        print("  Email: " + self.age)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nGood afternoon, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self_login_attempts = 0
betty = User('betty', 'smith', 'beesmith', '30', 'United States')
betty.describe_user()
betty.greet_user()
print("\nHere are Betty's login attempts...")
betty.increment_login_attempts()
betty.increment_login_attempts()
betty.increment_login_attempts()
print(f"Total login attempts: {str(betty.login_attempts)}.")
print("Resetting the login attempts now!")
betty.reset_login_attempts()
print(f"Login attempts have been reset to {str(betty.login_attempts)}.")

#9.6
class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type ='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []
    def show_flavors(self):
        print("\nHere are our flavours for today:")
        for flavor in self.flavors:
            print(flavor.title())
BJ = IceCreamStand('Ben and Jerrys')
BJ.flavors = ['cookies and cream', 'red velvet', 'chocolate']
BJ.describe_restaurant()
BJ.show_flavors()

#9.7
class Admin(User):

    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = []

    def show_privileges(self):
        print("\nAdmin privileges are:")
        for privilege in self.privileges:
            print(privilege)
murphy = Admin('Murph', 'Smith', 'b4tt33th', '20', 'Australia')
murphy.describe_user()
murphy.privileges = ['user management', 'account banning', 'user access']
murphy.show_privileges()

#9.8 (most copied from 9.3)
class User():

    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.age = age.title()
        self.location = location.title()

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Age: " + self.age)
        print("Location: " + self.location)

    def greet_user(self):
        print("\nGood afternoon, " + self.username + "!")

class Admin(User):

    def __init__(self, first_name, last_name, username, age, location):
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = Privileges()
class Privileges():

    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges are:")
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)

murphy = Admin('Murph', 'Smith', 'b4tt33th', '20', 'Australia')
murphy.describe_user()
murphy.privileges.show_privileges()
murphy_privileges = ['user management', 'account banning', 'user access']
murphy.privileges.privileges = murphy_privileges
murphy.privileges.show_privileges()

#9.10
from restaurant import Restaurant

moes = Restaurant("Moes", "burritos")
moes.describe_restaurant()
moes.open_restaurant()

#9.11
from user import Admin

bee = Admin('bee', 'smith', 'beesknees', '19', 'United States')
bee.describe_user()

bee_privileges = ['user management', 'account banning', 'user access']
bee.privileges.privileges = bee_privileges
print("\nThe admin has these privileges:")
bee.privileges.show_privileges()

#9.12
from admin import Admin
bee = Admin('bee', 'smith', 'beesknees', '19', 'United States')
bee.describe_user()

bee_privileges = ['user management', 'account banning', 'user access']
bee.privileges.privileges = bee_privileges
print("\nThe admin has these privileges:")
bee.privileges.show_privileges()

#9.13
from random import randint
class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)

d6 = Die()
rolls = []
for roll_num in range(10):
    roll = d6.roll_die()
    rolls.append(roll)
print("Ten rolls of a normal die result in:")
print(rolls)

d10 = Die(sides=10)
rolls = []
for roll_num in range(10):
    roll = d10.roll_die()
    rolls.append(roll)
print("Ten rolls of a ten sided die result in:")
print(rolls)

d20 = Die(sides=20)
rolls = []
for roll_num in range(10):
    roll = d20.roll_die()
    rolls.append(roll)
print("Ten rolls of a twenty sided die result in:")
print(rolls)
#i'm really glad i did this one... giving me some inspo for my python project!

#10.1
file = 'learning_python.txt'
print("\nHere's the file...")
with open(file) as f:
    contents = f.read()
print(contents)

print("\nHere's the text in a loop...")
with open(file) as f:
    for line in f:
        print(line.rstrip())
print("\nHere's the text in a list...")
with open(file) as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())

#10.2
file = 'learning_python.txt'
with open(file) as f:
    texts = f.readlines()
for text in texts:
    text = text.rstrip()
    print(text.replace('Python', 'C'))

#10.3
username = input("\nCould you tell me your name?")
file = 'guest.txt'
with open(file, 'w') as f:
    f.write(username)

#10.4
file = 'guest_book.txt'
print("\nType 'stop' when you're done!")
while True:
    username = input("Could you tell me your name?")
    if username == 'stop':
        break
    else:
        with open(file, 'a') as f:
            f.write(username)
        print(f"\n{username} has been added to the guest book!")

#10.5
file = 'programming_poll.txt'
answers = []
while True:
    answer = input("\nWhy do you like programming?")
    answers.append(answer)
    newanswer = input("Do you want to add any other reasons? Type 'no' to end the loop.")
    if newanswer == 'no':
        break
with open(file, 'a') as f:
    for answer in answers:
        f.write(answer)

#10.6
try:
    n = input("Enter a number:")
    n = int(n)
    m = input("Enter another number:")
    m = int(m)
except ValueError:
    print("I said a NUMBER.")
else:
    added = n + m
    print(f"{str(n)} and {str(m)} added together is {str(added)}.")

#10.7
print("Enter 'stop' to end the loop.")
while True:
    try:
        n = input("Enter a number:")
        if n == 'stop':
            break
        n = int(n)

        m = input("Enter another number:")
        if m == 'stop':
            break
        m = int(m)

    except ValueError:
        print("I said a NUMBER. Try again.")
    else:
        added = n + m
        print(f"{str(n)} and {str(m)} added together is {str(added)}.")

#10.8
files = ['cats.txt', 'dogs.txt']
for file in files:
    print(f"\nFile contents are {file}")
    try:
        with open(file) as f:
            text = f.read()
            print(text)
    except FileNotFoundError:
        print("Sorry, I couldn't find that.")

#10.9
files = ['cats.txt', 'dogs.txt']
for file in files:
    print(f"\nFile contents are {file}")
    try:
        with open(file) as f:
            text = f.read()
            print(text)
    except FileNotFoundError:
        pass

#10.11
import json
    with open('favnumber.json') as f:
        number = json.load(f)
print(f"\nI know your favourite number! It's {str(number)}.")

#10.12
import json
try:
    with open('favnumber.json') as f:
        number = json.load(f)
except FileExistsError:
    number = input("Could you tell me what your favourite number is?")
    with open('favnumber.json', 'w') as f:
        json.dump(number, f)
    print("Gotcha!")
else:
    print(f"I know your favourite number! It's {str(number)}.")

#10.13
import json
def get_old_username():
    file = 'username.json'
    try:
        with open(file) as f_obj:
            user = json.load(f_obj)
    except FileExistsError:
        return None
    else:
        return user

def get_new_username():
    user = input("Could you tell me your name?")
    file = 'username.json'
    with open(file, 'w') as f_obj:
        json.dump(user, f_obj)
    return user

def greet_user():
    user = get_old_username()
    if user:
        correct = input(f"Are you {user}? YES/NO.")
        if correct == 'YES':
            print(f"Long time no see, {user}!")
        else:
            user = get_new_username()
            print("We'll record you for next time.")
    else:
        user = get_new_username()
        print("We'll record you for next time.")
greet_user()

#Parallel vs Sequential processing
#Parallel processing seems more useful when tasks are more CPU heavy or computational and not reliant on input to
#continue! So if I prompted a user to input some numbers and do a bunch of different mathematical equations, parallel
#be more appropriate. But if I was trying to build a user profile, and was continuing to ask user for input, sequential
#makes more sense.