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
elif b>a:
    print(f"{b}>{a}")
else:
    print(f"{b}={a}")
    print("Not Hello!")

if a > b:
    print(f"{a}>{b}")
    print("Hello")
if b>a:
    print(f"{b}>{a}")
if a == b:
    print(f"{b}={a}")
    print("Not Hello!")

#Функції
def print_function():
    print("Hello")

print_function()

def square(a, b):
    res = a*b
    return res
    print("Hello square")

print (square(5, 10))
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

print(compare_2_numbers(10,4))
print(compare_2_numbers(5,10))
print(compare_2_numbers(4,4))