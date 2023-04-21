f = 5
f = 5.0

# def Square(first, second):
#     return first*second

a = 16
b = 10

# Оператори порівняння: >, <, <=, >=, == (перевірка на рівність), != (перевірка на нерівність)

if a > b:
    print(f"{a}>{b}")
    print("Hello")
elif b > a:
    print(f"{b}>{a}")
else:
    print(f"{b}={a}")
    print("Not Hello!")

if a > b:
    print(f"{a}>{b}")
    print("Hello")
if b > a:
    print(f"{b}>{a}")
if a == b:
    print(f"{b}={a}")
    print("Not Hello!")


# Функції
def print_function():
    print("Hello")

print_function()

def square(a, b):
    res = a * b
    return res
    print("Hello square")

print(square(5, 10))
w = square(a, b)


def compare_2_numbers(a, b):
    result = ""
    if a > b:
        result = f"{a}>{b}"
    if b > a:
        result = f"{b}>{a}"
    if a == b:
        result = f"{b}={a}"
    return result
    #
    # if a > b:
    #     return f"{a}>{b}"
    # if b > a:
    #     return f"{b}>{a}"
    # if a == b:
    #     return f"{b}={a}"


print(compare_2_numbers(10, 4))
print(compare_2_numbers(5, 10))
print(compare_2_numbers(4, 4))


def hello():
    return 'Hello everybody!'


def my_max(a, b):
    if a > b:
        result = a
    elif b > a:
        result = b
    else:
        result = 'Numbers are equal'
    return result


def my_test():
    a = 5
    b = 7
    result = a + b
    return result
    result = a * b
    return result


f = my_test()
print(f)


# Створити функцію sum_even_nums_in_range(start, stop), що отримує 2 параметри (start, stop), та повертає суму всіх парних чисел в діапазоні.
#
# sum_even_nums_in_range(10, 20) ➞ 90
# 10, 12, 14, 16, 18, 20
def sum_even_nums_in_range(start, stop):
    s = 0
    for i in range(start, stop + 1):
        if i % 2 == 0:
            s = s + i
    return s


my_list = [
    {"name": "John", "age": 21, "budget": 23000},
    {"name": "Steve", "age": 32, "budget": 40000},
    {"name": "Martin", "age": 16, "budget": 2700}
]
print(my_list)
for user in my_list:
    print(user['budget'])

budgets = sum([user['budget'] for user in my_list])
print(budgets)

total_budget = 0
for user in my_list:
    total_budget += user['budget']
print(total_budget)

name = 'iiiiiiii'
name_set = set(name)
print(len(name_set))


def d():
    student = {'Olena', 'Yuriy', 'Iryna', 'Serhii', 'Dmytro', 'Igor', 'Mariia'}
    st_1 = {'Olena', 'Yuriy', 'Iryna'}
    if not (st_1.issubset(student)):
        return False
    return True


f = [5, 4, 3, 9, 2, 7, 1, 1, 2, 3, 4, 5, 6, 3, 1]
set_1 = set(f)
print(set_1)
my_list = list(set_1)
my_list.sort()
print(my_list)
my_unique_list = list(set(f))
print(my_unique_list)



