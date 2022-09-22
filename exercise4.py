#1
Ben = {'f_name' : 'Ben',
       'l_name':'Mullikin',
       'age':'20',
       'hometown': 'anderson',
       'current_city': 'pendleton',
       'username' : 'benopolist'}
print(Ben)
print(Ben['f_name'])
print(Ben['l_name'])
print(Ben['age'])
print(Ben['hometown'])
print(Ben['current_city'])
print(Ben['username'])
#2
print(f"\nThis person's first name is {Ben['f_name']}, last name is {Ben['l_name']}, and their username is {Ben['username']}.")
print(f"For security reasons, we might ask them for their hometown, which is {Ben['hometown'].title()}.")
#3
definitions = {'python' : 'an interpretive programming language with dynamic semantics',
       'variable' : 'An object assigned a name',
       'list' : 'An ordered collection of objects',
       'method' : 'A function that belongs to a particular object',
       'if statement' : 'A conditional execution',
       'dictionary' : 'A collection of key and value pairs',
       'function' : 'A group of statements that performs a specific task',}
print(f"\nPython: \n{definitions['python']}.")
print(f"\nVariable: \n{definitions['variable']}.")
print(f"\nList: \n{definitions['list']}.")
print(f"\nMethod: \n{definitions['method']}.")
print(f"\nIf Statement: \n{definitions['if statement']}.")
print(f"\nDictionary: \n{definitions['dictionary']}.")
print(f"\nFunction: \n{definitions['function']}.")
#4
for key, value in definitions.items():
       print(f"\n{key.title()}:")
       print(f"{value}.")
#5
SC_counties = {'York County' : 'York',
       'Williamsburg County' : 'Kingstree',
       'Union County' : 'Union',
       'Sumter County' : 'Sumter',
       'Spartanburg' : 'Spartanburg',
       'Saluda County' : 'Saluda'}
#6
sccounties = ['York County', 'Williamsburg County', 'Union County', 'Sumter County', 'Spartanburg', 'Saluda County', 'Richland County', 'Pickens County', 'Orangeburg County', 'Oconee County']
for county in sccounties:
       if county in SC_counties:
              print(f"{county} is in our dictionary, and the county is {SC_counties[county]}.")
       else:
              print(f"{county} is not in our dictionary. We will add this county shortly. Thanks!")
#7
abbeville = {'Calhoun Falls' : '1,814',
       'Donalds' : '313',
       'Due West' : '1,189',
       'Honea Path' : '3,753',
       'Lowndesville' :'172'}
aiken = {'Burnettown' : '2,731',
         'Jackson' : '2,111',
         'Monetta' : '252',
         'New Ellenton' : '2,159',
         'Perry' : '236'}
anderson = {'Belton' : '4,436',
            'Clemson' : '16,917',
            'Honea Path' : '3,753',
            'Iva' : '1,177',
            'Pelzer' : '1,653'}
barnwell = {'Blackville' : '2,037',
            'Elko' : '327',
            'Hilda' : '461',
            'Kline' : '150',
            'Snelling' : '224',}
berkeley = {'Bonneau' : '1,801',
            'Charleston' : '137,041',
            'Goose Creek' : '42,944',
            'Hanahan' : '25,743',
            'North Charleston' : '113,880'}
county = [abbeville, aiken, anderson, barnwell, berkeley]
for x in county:
       for y in x:
              print(f"In {y}, the current population is {x[y]}.")
#8
sc_counties = {'Laurens County' : ['Clinton', 'Laurens', 'Cross Hill'],
               'Lexington County' : ['Cayce', 'Red Bank', 'Lexington'],
               'Newberry' : ['Newberry', 'Whitmire', 'Prosperity']}
for county, cities in sc_counties.items():
       print(f"\nIn {county}, the largest cities are:")
       for city in cities:
              print(f"{city}")
#User Input 1
message = input("\nGood afternoon, what is your name?")
print(f"Hello {message}, welcome to Anderson University!")
#User Input 2
message2 = input("\nHow much money have you budgeted for a new processor?")
message2 = int(message2)
if message2 >= 500:
    print("\nYou have budgeted enough to buy an i9, i7, i5, or i3 processor!")
elif message2 >= 350:
    print("\nYou have budgeted enough to buy an i7, i5, or i3 processor!")
elif message2 >= 120:
    print("\nYou have budgeted enough to buy an i5 or i3 processor!")
elif message2 >= 75:
    print("\nYou have budgeted enough to buy an i3 processor!")
elif message2 <= 74:
    print("\nI'm sorry, but our cheapest processor chip is $75.")
#User Input 3
number = "\nGive us a number and we will check if it is odd or even!\n Enter '0' when finished."
answer = ""
while True:
    answer = int(input(number))
    if answer == 0:
        print('Goodbye then!')
        break
    elif answer % 2 == 0:
        print(f"\nThe number {answer} is even!")
    else:
        print(f"\nThe number {answer} is odd!")
#User Input 4
prompt = "\nWhat fruit does shinigami love? "
while True:
    response = input(prompt)
    if response == 'no thanks':
        print('No worries! See you later.')
        break
    elif response == 'apples':
        print("You guessed it! You're so smart. Type 'apples' for more validation, or type 'no thanks' to quit.")
    else:
        print("That's not quite right. Try again, or enter 'no thanks' to quit.")

#User Input 5
pollanswers = {}
poll_active = True
while poll_active:
    name = input("\nWhat is your username?" )
    answered = input("What is your favourite Ubuntu flavour?" )
    pollanswers[name] = answered
    finish = ("Are you done polling? Type 'yes' for results or 'no' for more entries.")
    if finish == 'yes':
        poll_active = False
    print("\n----Results of the Poll!----")
    for name, answered in pollanswers.items():
        print(f"{name.title()}:\nYour favourite Ubuntu flavour is {answered.title()}!")
