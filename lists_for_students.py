# list - список
# tuple - кортежі
# dict - словник
# set - множина

# Оголошення порожнього списку
numbers = []
numbers = list()

people = ["Igor", "Oleg", "Andrii"]
numbers = [1, 2, 3, 4]

objects = [1, 5.6, True, 'Ukraine']
print(people)

# Використання конструктора list
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list(numbers1)
print(numbers2)

word = "Ukraine"
letters = list(word)
print(letters)

# Використання * при створенні списку
numb = [1] * 7
print(numb)

person = ['Tom'] * 5
print(person)

students = ['Bob', 'Sam'] * 3
print(students)

# Звертання до елементів списку
# здійснюється за індексом. Індекс першого елементу масиву - 0
l = 6
print(students[l - 1])
print(letters[0])

print(letters[-1])
print(letters[-3])

# Розкладання списку
people = ["Igor", "Oleg", "Andrii"]
igor, oleg, andrii = people
print(igor)

# Перебір елементів списку
people = ["Igor", "Oleg", "Andrii"]
for person in people:
    print(person)
    person += "!"

# len() - повертає кількість елементів в списку
i = 0
while i < len(people):
    print(people[i])
    people[i] += "!"
    i += 1

print(people)

# Перевірка списків на рівність
numbers1 = [1, 2, 3, 5, 4]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")

# Отримання частини списку
# people [:end] - повертає список від початку до end (не включно) [0,end)
# people [start:end] - повертає список від start (включно) до end (не включно) [start,end)
# people [start:end:step] - повертає список від start (включно) до end (не включно) з кроком step [start,end)
people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

slice_1 = people[:3]
print(slice_1)

slice_2 = people[1:4]
print(slice_2)

slice_3 = people[1:10:2]
print(slice_3)

slice_4 = people[:-1]
print(slice_4)

slice_5 = people[-3:-1]
print(slice_5)

# Методи для роботи зі списками
# Додавання та видалення елементів зі списку
people = ['Igor', 'Oleg']
# append() - додавання елементу в кінець списку
people.append('Andrii')
print(people)
# extend() - розширює існуючий список іншим списком
people.extend(['Ivan', 'Petro', 'Ivan'])
print(people)
# insert() - додавання елемента на вказану позицію
people.insert(1, 'Ivan')
print(people)
# index() - повертає індекс елемента
index_of_oleg = people.index('Oleg')
print(index_of_oleg)
# pop() - видаляє елемент за вказаним індесом
removed_element = people.pop(3)
print(people)
print(removed_element)
people.pop()
print(people)
# remove() - видаляє елемент за вказаним значенням
people.remove('Ivan')
print(people)
# clear() - повністю очищує список
people.clear()
print(people)

# Перевірка на наявність елементу в списку
people = ['Igor', 'Alice', 'Tetiana']
# people.remove('Andrii')
if 'Andrii' in people:
    people.remove('Andrii')

# оператор видаляє елемент зі списку
del people[-1]
print(people)

# Підрахунок кількості входжень елементу в список
people = ['Igor', 'Alice', 'Tetiana', 'Tetiana', 'Tad']
tetiana_count = people.count('Tetiana')
print(tetiana_count)

# Сортування
people.sort()
print(people)
people.reverse()
print(people)

people = ['Igor', 'alice', 'Tetiana', 'Tetiana', 'Tad']
people.sort()
print(people)

# сортування без врахування регістру
people.sort(key=str.lower)
print(people)

# пошук мінімального та максимального значення
numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))
print(max(numbers))

# Об'єднання списків
people1 = ["Tom", "Bob", "Alice"]
people2 = ["Tom", "Sam", "Tim", "Bill"]
people_3 = people1 + people2
print(people_3)

# Список списків
people_with_age = [['Igor', 18], ['Alice', 19], ['Tetiana', 25]]

print(people_with_age[1])
print(people_with_age[1][1])
# people_with_age.append('+380044334232')
# print(people_with_age)
people_with_age[1].append('+380044334232')
print(people_with_age)

for person in people_with_age:
    for item in person:
        print(item, end=" |")
    print()

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for fruit in fruits:
    if 'a' in fruit:
        newlist.append(fruit)
print(newlist)

# syntax: newlist_name = [вираз for елемент in iterable]
# syntax: newlist_name = [вираз for елемент in iterable [if умова==True]]
x = [1, 2, 3, 4, 5, 6]
x2 = []
for el in x:
    x2.append(el * el)
print(x2)
x2 = [el * el for el in x]
print(x2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_a)

# dictionary comprehension
# syntax: newlist_name = {ключ: значення for елемент in iterable}
# syntax: newlist_name = {ключ: значення for елемент in iterable [if умова==True]}
x = [1, 2, 3, 4, 5, 6]
# {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
square_dict = {num: num * num for num in x}
print(square_dict)

#
x = [1, 2, 3, 4, 5, 6]
new_x = [num ** 3 for num in x if num % 2 == 0]
print(new_x)

x = [1, 6, 7, 8, 10, 11]
# Знайти суму всіх елементів списку, які знаходяться до першого парного елементу
s = 0
for num in x:
    if num % 2 == 0:
        break
    s += num
print(s)
# Знайти суму всіх непарних елементів списку
s = 0
for num in x:
    if num % 2 != 0:
        s += num
print(s)

s = 0
for num in x:
    if num % 2 == 0:
        continue
    s += num
print(s)