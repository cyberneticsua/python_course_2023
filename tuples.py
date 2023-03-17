#Кортеж - послідовність елементів, він є змінювати
tom = ("Tom", 23)
print(tom)

igor = "Igor", 33
print(igor)

igor = ("Igor", )
print(igor)

my_list = ['Igor', 33, 'Ukraine', 'Cybernetics']
igor = tuple(my_list)
print(igor)
print(len(igor))

print(igor[0])
print(igor[1])
print(igor[2])
print(igor[3])
print(igor[-1])

name, age, country, university = igor
print(name)
print(age)
print(country)
print(university)

#Отримання підкортежів
print(igor[1:3])
print(igor[:3])
print(igor[1:])

def get_user_data():
    name = "Kateryna"
    age = 17
    company = 'ChNU'
    return name, age, company

user = get_user_data()
print(user)

def print_information(name, age, company):
    print(f'Name: {name} Age: {age} Company: {company}')

tetiana = ('Tetiana', 18)
print_information(*tetiana, 'Microsoft')

kateryna = ('Kateryna', 19, 'Apple')
print_information(*kateryna)

#перебір кортежів
kateryna = ('Kateryna', 19, 'Apple')
for item in kateryna:
    print(item)

#перевірка наявності значення в кортежі
kateryna = ('Kateryna', 19, 'Apple')
name = 'Kate'
if name in kateryna:
    print('Елемент присутній в кортежі')