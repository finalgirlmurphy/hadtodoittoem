#8.3
def make_shirt(size, text):
    """Describes a shirt text and size being printed."""
    print(f"\nLet's make a dope {size} shirt!")
    print(f'My cool shirt will say "{text}".')
make_shirt('XL', 'Women want me, fish fear me')
make_shirt(size="XS", text="CAUTION: bites")
#8.4
def make_shirt(size='L', text='I love Python!'):
    """Makes all printed shirts large by default"""
    print(f"\nLet's make a cool {size} shirt!")
    print(f'My dope shirt will say "{text}".')
make_shirt()
make_shirt(size='M')
make_shirt(size='S', text='CTF Rocks')
#8.5
def describe_city(city, country='australia'):
    """Describes a country and city"""
    print(f"\nThe city {city.title()} is in the beautiful {country.title()}!")
describe_city(city='Palmerston')
describe_city(city='bunbury')
describe_city(city='christchurch', country='new zealand')
#8.6
def city_country(city, country):
    """Return a city, country string"""
    citycountry = f"\n{city}, {country}."
    return citycountry.title()
city = city_country('canberra', 'australia')
print(city)
city = city_country('edinburgh', 'scotland')
print(city)
city = city_country('hastings', 'australia')
print(city)
#8.7
def make_album(artist, album, tracks=''):
    albumdict = {'artist': artist,
                 'album': album}
    if tracks:
        albumdict['tracks'] = tracks
    return albumdict

album = make_album('Type O Negative', 'October Rust')
print(album)
album = make_album('Siouxsie and the Banshees', 'Juju', tracks ='12')
print(album)
album = make_album('Muse', 'Absolution')
print(album)
#8.8
enter_album = "What's your favourite album? "
enter_artist = "\nCool! Which artist made that? "
print("\nEnter 'stop' to end the loop.")
while True:
    title = input(enter_album)
    if title == 'stop':
        break
    artist = input(enter_artist)
    if artist == 'stop':
        break
    music = make_album(artist, title)
    print(music)
#8.9
def show_messages(texts):
    for text in texts:
        print(f"\n{text}")
texts = ['gtg', 'brb', 'ily']
show_messages(texts)
#8.10
def show_messages(texts):
    for text in texts:
        print(f"\n{text}")

def send_messages(texts, sent_messages):
    while texts:
        textmessages = texts.pop()
        print(textmessages)
        sent_messages.append(textmessages)

texts = ["hi!", "where r u", "bye!"]
show_messages(texts)
sent_messages = []
send_messages(texts, sent_messages)
print(f"\n{texts}")
print(sent_messages)
#8.11
def show_messages(texts):
    for text in texts:
        print(f"\n{text}")

def send_messages(texts, sent_messages):
    while texts:
        textmessages = texts.pop()
        print(textmessages)
        sent_messages.append(textmessages)

texts = ["hi!", "where r u", "bye!"]
show_messages(texts)
sent_messages = []
send_messages(texts[:], sent_messages)
print(f"\n{texts}")
print(sent_messages)
#8.12
def sandwhich_items(*items):
    print("\nTime to make a cool sandwich!")
    for item in items:
        print(f"Let's add {item} to the sandwich!")
sandwhich_items('swiss cheese', 'saurkraut','thousand island sauce', 'pastrami')
sandwhich_items('peanut butter', 'jelly', 'marshmallow fluff')
sandwhich_items('butter', 'hundreds and thousands')
#8.13
def build_profile(first, last, **user_info):
    user_info['First_Name'] = first
    user_info['Last_Name'] = last
    return user_info
userprofile = build_profile('Murphy', 'Smith', Favourite_Song = 'Black no. 1', Favourite_Drink = 'Lychee Boba', Hometown = 'Palmerston')
print(f"\n{userprofile}")
#8.14
def make_car(manufacturer, model, **otherstuff):
    cardictionary = {'manufacturer': manufacturer,
                     'model' : model}
    for x, y in otherstuff.items():
        cardictionary[x] = y
    return cardictionary
car = make_car('kia', 'soul', color = 'grey', seat_warmers = 'no')
print(f"\n{car}")
#8.15 (I had to google the example text for printing_functions.py as I could not find it in the text... and miss annie nastasi helped.)
import printing_functions
unprinted_designs = ['slug toy', 'fidget ball', 'statue', 'charm']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#8.16
import citycountry
from citycountry import city_country
from citycountry import city_country as cities
import citycountry as countrycity
from citycountry import *
#8.17
#I checked 8.5-8.7 and all of them had spacing around the '=', which I corrected!
#I did not use any outside sources other than googling the example printing text, but Annie Nastasi helped lots :D
