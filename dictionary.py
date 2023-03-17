# словник1 = {ключ1: значення, ключ2:значення}
users = {1: "Igor", 2: 'Tetiana', 3: 'Kateryna'}

users = {'igor@chnu.edu.ua': "Igor", 'tetiana@chnu.edu.ua': 'Tetiana', 'kateryna@chnu.edu.ua': 'Kateryna'}

users = {1: 'Igor', 'tetian@gmail.com': 'Tetiana', True: 'One more user'}
# Оголошення порожнього словника
users = {}
objects = dict()

# Перетворення списку та кортежу в словник
users_list = [
    ['+3805554334', 'Tom'],
    ['+3805554322', 'Bill'],
    ['+3805554311', 'Bob'],
]
users_dict = dict(users_list)
print(users_dict)

users_tuple = (
    ('+3805554334', 'Tom'),
    ('+3805554322', 'Bill'),
    ('+3805554311', 'Bob'),
)
users_dict = dict(users_tuple)
print(users_dict)

# Отримання значення елементів
users = {'igor@chnu.edu.ua': "Igor",
         'tetiana@chnu.edu.ua': 'Tetiana',
         'kateryna@chnu.edu.ua': 'Kateryna'}
print(users['igor@chnu.edu.ua'])
users['igor@chnu.edu.ua'] = 'Bob'
print(users['igor@chnu.edu.ua'])
users['billi@chnu.edu.ua'] = 'Billi'
print(users)
if 'georgi@chnu.edu.ua' in users:
    print(users['georgi@chnu.edu.ua'])
else:
    print('Елемент не знайдено')

print(users.get('georgi@chnu.edu.ua')) #None
print(users.get('georgi@chnu.edu.ua', 'Елемент не знайдено'))
print(users.get('billi@chnu.edu.ua'))

# Видалення елементів зі словника
del users['igor@chnu.edu.ua']
print(users)
if 'igor@chnu.edu.ua' in users:
    del users['igor@chnu.edu.ua']

# Метод pop
users = {'igor@chnu.edu.ua': "Igor",
         'tetiana@chnu.edu.ua': 'Tetiana',
         'kateryna@chnu.edu.ua': 'Kateryna'}
user = users.pop('igor@chnu.edu.ua')
print(users)
print(user)
user = users.pop('igor@chnu.edu.ua', 'Елемент не знайдено')

# Очистка словника
users.clear()

# Копіювання словника
users = {'igor@chnu.edu.ua': "Igor",
         'tetiana@chnu.edu.ua': 'Tetiana',
         'kateryna@chnu.edu.ua': 'Kateryna'}
students = users.copy()
print(students)

users_2 = {'igor1@chnu.edu.ua': "Igor",
           'tetiana1@chnu.edu.ua': 'Tetiana'}

users.update(users_2)
print(users)

# Перебір елементів словника
users = {'igor@chnu.edu.ua': "Igor",
         'tetiana@chnu.edu.ua': 'Tetiana',
         'kateryna@chnu.edu.ua': 'Kateryna'}
for key in users:
    print(f'User {key} User value {users[key]}')

for key, value in users.items():
    print(f'User {key} User value {value}')

for key in users.keys():
    print(f'User {key}')

for value in users.values():
    print(f'Values {value}')

# Використання комплексних словників
users = {
    'Igor': {
        'phone': '+379443344',
        'email': 'igor@chnu.edu.ua'
    },
    'Tetiana': {
        'phone': '+379443344',
        'mobile': '+309474405',
        'email': 'igor@chnu.edu.ua'
    }
}
print(users['Igor']['phone'])
users['Igor']['mobile'] = '384234855'
print(users['Igor'])
for key, value in users.items():
    print(f'Користувач {key}')
    for element, val in value.items():
        print(f'{element} - {val}')
