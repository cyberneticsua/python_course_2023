message = 'Hello'
message = "Hello"

long_message = ('My first row \n'
                'My second row')
print(long_message)

text = '''My first row
my second row
'''
print(text)

message = 'М\'яч'
print(message)

# \' - додає одинарні лапки в рядок
# \" - додає подвійні лапки в рядок
# \n - додає абзац в рядок
# \t - додає табуляцію (4 пробіли) в рядок

# Вставка значень в рядок
user_name = "Igor"
user_age = '21'
user = f'Name {user_name} віком {user_age}'
print(user)

# Звертання до символів рядка
country = 'Ukraine'
print(country[0])
print(country[-1])

# Перебір кожного елемента рядка
for char in country:
    print(char, end='-')
print()
# Отримання підрядка
# string [:end] - отримує з рядка підрядок, починаючи з початку рядку до end (не включно), country[:3]
# string [start:end] - отримує з рядка підрядок, починаючи з start до end (не включно), country[1:3]
# string [start:end:step] - отримує з рядка підрядок, починаючи з start до end з кроком step (не включно), country[0:5:2]

print(country[:3])
print(country[1:3])
print(country[0:5:2])

# Обєднання рядків
name = "Igor"
surname = "Vinnychuk"
full_name = name + ' ' + surname
print(full_name)

# Повторення рядків
name = 'i' * 5
print(name)
name = 'he' * 5
print(name)

# Порівняння рядків
str1 = '1a'
str2 = 'aa'
str3 = 'Aa'
print(str1 > str2)
print(str2 > str3)

str1 = 'igor'
str2 = 'Igor'
print(str1.lower() == str2.lower())
print(str1.upper() == str2.upper())

# Функції len та ord
print(ord('I'))
print(len(country))

# Пошук в рядках
string = "Hello Ukraine"
exist = "Hello" in string
print(exist)
exist = "hello" in string
print(exist)

# Перевірка рядків
# isalpha() - повертає True, якщо рядок складається тільки з символів абетки
# isdigit() - повертає True, якщо всі символи рядка - цифри
# isnumeric() - повертає True, якщо рядок може бути числом
# islower() - повертає True, якщо всі символи рядка в нижньому регістрі
# isupper() - повертає True, якщо всі символи рядка в верхньому регістрі

number = '111123'
if number.isnumeric():
    print(int(number)*5)

#startswith(str) - повертає True, якщо рядок починається з підрядка str
#endswith(str) - повертає True, якщо рядок закінчується на підрядок str
string = "Hello Ukraine"
print(string.startswith('Hello'))
print(string.endswith('Hello'))

#upper() - переводить весь рядок у верхній регістр
#lower() - переводить весь рядок у нижній регістр
#title() - переводить у верхній регістр всі слова в рядку
#capitalize() - перевеодить у верхній регістр тільки перше слово в рядку
string = "london is a capital of great britain. London is great city."
print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())
upper_string = string.upper()
print(upper_string)

#lstrip() - видаляє всі пробіли на початку рядка
#rstrip() - видаляє всі пробіли в кінці рядка
#strip() - видаляє всі пробіли на початку і в кінці рядка
#ljust(width) - якщо довжина рядка менша за width, то справа до рядка додаються пробіли, щоб довжина рядка стала дорівнювати width
#rjust(width) - якщо довжина рядка менша за width, то зліва до рядка додаються пробіли, щоб довжина рядка стала дорівнювати width
#center(width) - якщо довжина рядка менша за width, то зліва та справа до рядка рівномірно додаються пробіли, щоб довжина рядка стала дорівнювати width
string = "Hello Ukraine"
print(string.ljust(20))
print(string.rjust(20))
print(string.center(20))

#Пошук в рядку
#find(str) - пошук підрядка str ведеться з початку рядка і до його кінця
#find(str, start) - пошук підрядка str ведеться з позиції start і до його кінця
#find(str, start, end) - пошук підрядка str ведеться з позиції start і до позиції end
string = "Hello Ukraine"
print(string.find('Ukr'))
print(string.find('Ukr', 8))
print(string.find('Ukr', 5, 9))

#Заміна в рядку
#replace(old, new) - замінює підрядок old на підрядок new
#replace(old, new, num) - замінює підрядок old на підрядок new num-разів

phone = "+38-050-666-55-44"
new_phone = phone.replace('-', ' ')
print(new_phone)
new_phone = phone.replace('-', ' ', 1)
print(new_phone)

#Розділення рядків
#split - повертає список рядків, розділених за допомогою певного символа
#split() - використовує як роздільник пробіл
#split(str) - використовує як роздільник символ str
#split(str, num) - використовує як роздільник символ str, а num вказує скільки входжень str використовується для розділення
string = 'London is a  capital of  Great  Britain. London is great city.'
words = string.split()
print(words)
words = string.split(' ')
print(words)
words = string.replace('.', '').replace(',', '').split()
print(words)

#Зєднання рядків
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
sentence = "|||".join(words)
print(sentence)