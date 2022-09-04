
# This is a program to store new vehicle inventory and assist with monthly payments
# Create variable of your favorite car brand
favbrand = 'kia'
# Create list of 5 of their models from cheapest to most expensive
kiamodels = ['rio', 'soul', 'forte', 'k5', 'stinger']
# Append a 6th model to the list
kiamodels.append('sorento')
# Create list of 5 standard colors for all models
kiacolours = ['space grey', 'mars orange', 'cherry black', 'neptune blue', 'solar yellow']
# Replace your last color with a different color
kiacolours[4] = 'inferno red'
# Create variable of the current new year models
newyear = ('2023')
# Create MSRP constant number (not string) of each of the models
rio, soul, forte, k5, sorento = 16450, 19790, 19490, 25090, 36590
# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans
fouryear = 48
fiveyear = 60
sixyear = 72
# Create a variable for the guest's name. Be courteous in your upcoming messages :)
guest = 'my guy'
# Create message variable (with f-string) welcoming customer to your new car store
coolwelcome = f"welcome to the jungle baby girl. how can i help you, {guest}?"
# Create awesome banner with your brand/name/dealership, however you want to welcome customers
banner = "꧁༺ 𝓶𝓾𝓻𝓹𝓱𝔂𝓼 𝓵𝓲𝓰𝓱𝓽𝓵𝔂 𝔀𝓻𝓮𝓬𝓴𝓮𝓭 𝓬𝓪𝓻𝓼 ༻꧂"
# Print awesome banner and welcome message
print(banner, coolwelcome, sep='\n')
# Using title methods, print the number vehicles in alphabetical order, with the year and available colors.
models= sorted(kiamodels)
colours = sorted(kiacolours)
print(f"{newyear}", "models available are:", (models[0]),(models[1]), (models[2]), (models[3]), (models[4])
      , "\nin colours such as:", (colours[0]), (colours[1]), (colours[2]), (colours[3]), (colours[4]))
# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the first vehicle
import math
fortepaymentsfive = math.ceil(forte / 60)
# and print that in a nice, kind message. Don't be rude/pushy to the customer :)
print("hey,", (guest), "if you're interested in the", (models[0]), "a five year monthly plan would be this amount monthly:",
      (fortepaymentsfive))
# Do the same thing, but give them 4yr and 6yr options for the same vehicle
print( (guest), "if you want some other options, you can do a four year plan for", math.ceil(forte / fouryear),
"or a six year plan for", math.ceil(forte / sixyear), "USD monthly" )
# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested
print( "if you are interested in the", (models[1]),", a five year plan in mothly USD payments would be", math.ceil(k5/fiveyear))
print( "if you are interested in the", (models[2]),", a five year plan in mothly USD payments would be", math.ceil(rio/fiveyear))
print( "if you are interested in the", (models[3]),", a five year plan in mothly USD payments would be", math.ceil(sorento/fiveyear))
print( "if you are interested in the", (models[4]),", a five year plan in mothly USD payments would be", math.ceil(soul/fiveyear), ". \nlet me know if you would like to test drive any of the models :D")
# feature 1 is the first years payment for a forte with 5% yearly interest on a 4 year plan, rounded up for the sake of even numbers:)
yearonepaymenttotal= f"i see you are interested in the forte with a four year plan, " \
                     f"the total of payments for your first year would total to {math.ceil(forte/fouryear) * 12 * 1.05}"
print(yearonepaymenttotal)
# feature 2 is a a total of how many model colours are available
colourfeature = f"we have an impressive range of colours available, a grand total of {len(colours)} colours to choose from"
print(colourfeature)
#feature 3 uses an f string for the car dealership owner to brag about their own model
dunkonem = f"my own kia is the mom van shaped {models[3]}! lots of room for sports equipment " \
           f"in the back of this bad boy :). mine is in the sexiest colour, {colours[1]} ."
print(dunkonem)