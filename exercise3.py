# hi brandon! :D
# 5-1
brand = 'Kat Von D'
print("Is brand == 'Black Moon Cosmetics'? I predict False.")
print(brand == 'Black Moon Cosmetics')
print("Is brand == 'Lime Crime'? I predict False.")
print(brand == 'Lime Crime')
print("Is brand == 'Lunar Beauty'? I predict False.")
print(brand == 'Lunar Beauty')
print("Is brand == 'Kat Von D'? I predict True.")
print( brand == "Kat Von D")

car = 'Kia'
print("\nIs car == 'Audi'? I predict False.")
print(car == "Audi")
print("Is car == 'Nissan'? I predict False.")
print(car == "Nissan")
print("Is car == 'Toyota'? I predict False.")
print(car == "Toyota")
print("Is car == 'Kia'? I predict True.")
print(car == "Kia")

food = "Gyros"
print("\nIs food == 'Gryos'? I predict True.")
print( food == 'Gyros')

os = "Mac"
print("\nIs os == 'Mac'? I predict True.")
print( os == 'Mac')

drink = "Boba"
print("\nIs drink == 'Boba'? I predict True.")
print( drink == 'Boba')
#5-2
movies = ['Coraline', 'Rocket Man', 'Mr. Fox', 'HTTYD']
movies2 = ['Coraline', 'Rocket Man']
movies3 = ['Coraline', 'Rocket Man', 'Mr. Fox', 'HTTYD']
print("\n 5-2 \n Does movies == movies2? I predict false")
print(movies == movies2)
print("Does movies == movies3? I predict true")
print(movies == movies3)
print("Does movies != movies2? I predict true")
print(movies != movies2)
print("Does movies != movies3? I predict false")
print(movies != movies3)

movie = "Nope"
print(movie == 'nope')
print(movie.lower() == 'nope')

number = 1
number2 = 3
number3 = 9
print(number ==1)
print(number!= 1)
print(number > number2)
print(number < number2)
print(number2 >= number3)
print(number2 <= number3)
number < number2 and number < number3
number2 > number3 or number2 > number

bestmovie = 'Coraline'
worstmovie = 'Lolita'
if bestmovie not in movies:
    print(f"We don't have {bestmovie}")
else:
    print(f"\nWe have {bestmovie}!")
if worstmovie not in movies:
    print(f"Thank god, we threw {worstmovie} out.")
else:
    print(f"Ew, why do we have {worstmovie}?")
#5-3
alien_color = 'Green'
if alien_color == 'Green':
    print('\nYou earned 5 points!')
if alien_color != 'Green':
    print('No points earned')
#5-4
alien_colour = 'Red'
if alien_colour == 'Green':
    print("\nYou earned 5 points!")
else:
    print("You earned 10 points!")
#5-5
if alien_color == 'Green':
    print("\nYou earned 5 points!")
elif alien_color == 'Yellow':
    print("You earned 10 points!")
elif alien_color == 'Red':
    print("You earned 15 points!")
#5-6
age = 25
if age < 2:
    print("You're a baby.")
elif ((age >= 2) and (age < 4)):
    print("You're a toddler.")
elif ((age >= 4) and (age < 13)):
    print("You're a kid.")
elif ((age >= 13) and (age < 20)):
    print("You're a teenager.")
elif ((age >= 20) and (age < 65)):
    print("\nYou're an adult.")
elif age > 65:
    print("You're an elder.")
#5-7
favourite_fruits = ['Lychee', 'Blackberry', 'Mango']
if 'Lychee' in favourite_fruits:
    print("\nI'd sell a kidney for a lychee right now.")
if 'Strawberry' in favourite_fruits:
    print("\nI'd sell a kidney for a strawberry right now.")
if 'Rockmelon' in favourite_fruits:
    print("\nI'd sell a kidney for a rockmelon right now.")
#5-8
users = ['user1', 'user2', 'user3', 'user4', 'admin']
for user in users:
    if user == 'admin':
        print(f"\nGood afternoon {user}, would you like to view user activity?")
    else:
        print(f"\nGood afternoon {user}, nice to see you again!")
#5-9
users = []
for user in users:
    if user == 'admin':
        print(f"\n Good afternoon {user}, would you like to view user activity?")
    else:
        print(f"\nGood afternoon {user}, nice to see you again!")
else:
    print("\nWe need to find some users!")
#5-10
current_users = ['user5', 'user6', 'user7', 'user8', 'user9', 'user10']
new_users = ['user9', 'user10', 'user11', 'user12', 'user13']
current_userslowercase = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_userslowercase:
        print(f"\nSorry bud, {new_user} is taken. Pick a new username!")
    else:
        print(f"\n{new_user} is available!")
#5-11
numberslist = list(range(1,10))
for number in numberslist:
    if number == 1:
        print("\n1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
#5-12 and 13
#i think i've styled everything appropriately, though I had to ask a friend for help on 5-10 to copy the list in lowercase, i was just confused.
#my dream is to create a simple game that rickrolls dr. knapp in an even more severe way. i think if i can rickroll him twice i will die happy.
#this feat will take some creative social engineering, but i think i can pull it off :)