states = {
    'Россия': "RU",
    'Германия':"DE",
    'Узбекистан': "UZ",
    'Зимбабве' : "ZW",
    "Турция" : "TR"
}

cities = {
    "UZ": "Гаэли",
    "TR": "Сарыгерме",
    "DE": "Мюнхен"
}

cities['ZW'] = "Гверу"
cities['RU'] = 'Москва'

print('-' * 10)
print(cities['RU'])

print('-' *20)
print(states['Турция'])

print("-" *30)
print(cities[states['Турция']])

print('-'*50)
for state, abbrev in list(states.items()):
    print(f'{state} {abbrev}')
    
print("-" * 100)
for state, abbrev in list(states.items()):
    print(f'{state}   {abbrev}   {cities[abbrev]}')
    
print('-' *200)

state = states.get('США')

if not state:
    print('Прошу прощения, США не существует или уничтожены')
    
city = cities.get('US', 'не существует')
print(f'в стране "US" есть город: {city}')