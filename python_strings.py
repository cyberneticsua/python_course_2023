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

#\' - додає одинарні лапки в рядок
#\" - додає подвійні лапки в рядок
#\n - додає абзац в рядок
#\t - додає табуляцію (4 пробіли) в рядок

#Вставка значень в рядок
user_name = "Igor"
user_age = '21'
user = f'Name {user_name} віком {user_age}'
print(user)

#Звертання до символів рядка
country = 'Ukraine'
print(country[0])
print(country[-1])

#Перебір кожного елемента рядка
for char in country:
    print(char, end='-')
print()
#Отримання підрядка
#string [:end] - отримує з рядка підрядок, починаючи з початку рядку до end (не включно), country[:3]
#string [start:end] - отримує з рядка підрядок, починаючи з start до end (не включно), country[1:3]
#string [start:end:step] - отримує з рядка підрядок, починаючи з start до end з кроком step (не включно), country[0:5:2]

print(country[:3])
print(country[1:3])
print(country[0:5:2])

#Обєднання рядків
name = "Igor"
surname = "Vinnychuk"
full_name = name + ' ' + surname
print(full_name)

#Повторення рядків
name = 'i' * 5
print(name)
name = 'he' * 5
print(name)

#Порівняння рядків
str1 = '1a'
str2 = 'aa'
str3 = 'Aa'
print(str1 > str2)
print(str2 > str3)

str1 = 'igor'
str2 = 'Igor'
print(str1.lower() == str2.lower())
print(str1.upper() == str2.upper())

#Функції len та ord
print(ord('I'))
print(len(country))

#Пошук в рядках
string = "Hello Ukraine"
exist = "Hello" in string
print(exist)
exist = "hello" in string
print(exist)


