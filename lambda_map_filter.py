from itertools import zip_longest

# list comprehension
double_odds = [n * 2 for n in range(10) if n % 2 == 1]

# zip function
ar1 = [3, 11, 2]
ar2 = [5, 6, 6]
n = len(ar1)
s = 0
for i in range(0, n):
    s += ar1[i] * ar2[i]

print(list(zip(ar1, ar2)))
mult = sum([a * b for a, b in zip(ar1, ar2)])
print(mult)

s = 'abc'
t = (11, 22, 33)
u = [94, 33, 22]
print(list(zip(s, t, u)))

s = 'abc'
t = (11, 22, 33, 44, 55)
u = [94, 33, 22, 555]
print(list(zip(s, t, u)))
print(list(zip_longest(s, t, u)))

students = ['Igor', 'Andriy', 'Tetiana']
ages = (22, 33, 44)
print(dict(zip(students, ages)))

# лямбда-вирази - це невеликі анонімні функції. Визначаються за допомогою оаератора lambda.
# lambda [параметри] : інструкції
message = lambda: print('Hello')
message()


def message():
    print("Hello")


# def vs lambda
# def - це ключове слово, яке не повертає нічого, але створює ім'я в локальному просторі імен
# lambda - повертає об'єкт-функцію, але не створює ім'я в локальному просторі імен
# def - може містити довільний python code
# lambda - він повинен містити код, який можна записати у вигляді виразу, тому не можу містити такі речі import, print, ...
def add(x, y):
    return x + y


Ladd = lambda x, y: x + y


def f1(x, y):
    if y == None:
        y = 10
    return x * y


Lf1 = lambda x, y: x * (y if y != None else 10)
# функція map повертає об'єкт типу map (який є ітерованим) і є результатом застосування заданої функції до кожного елементу об'єкту, який був
# переданий у map
# map(fun, iter) - fun - функція, яка повинна бути застосована до кожного елемента, iter - ітерований об'єкт, до якого повинна бути застосована функція
my_list = [1, 4, 5, 6, 7, 8, 8, 8, 6, 5, 4, 6, 7]
double_list_1 = [el*2 for el in my_list]
print(double_list_1)
double_list_2 = list(map(lambda x: x*2, my_list))
print(double_list_2)

#функція filter повертає ітератор, в якому елементи відсортовані відповідно до функції, яка задана яка параметр
# filter(fun, iter) - fun - функція, яка повинна бути застосована до кожного елемента, iter - ітерований об'єкт, до якого повинна бути застосована функція
#Відфільтрувати список, відобразивши в ньому тільки елементи, що більші за 16
ages = [11, 22, 33, 44, 55, 66, 77, 11, 11]
def filter_ages(x):
    if x<16:
        return False
    else:
        return True
ages_filter = list(filter(filter_ages, ages))
print(ages_filter)
ages_filter_lambda = list(filter(lambda x: x > 16, ages))
print(ages_filter_lambda)