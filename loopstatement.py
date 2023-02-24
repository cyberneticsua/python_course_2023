# В Python є 2 види циклів: while i for.
# Синтаксис while:
# while (умова):
#   оператори

# Вивести значення від 1 до 5.
print(1)
print(2)
print(3)
print(4)
print(5)

i = 1
# while i<6:
while i <= 5:
    print(i)
    i = i + 1
    # i += 1

# range(start, stop) - повертає діапазон [start, stop) range(1,10) - (1,2,3,4,5,6,7,8,9)
# range(start, stop, step) - повертає діапазон [start, stop) з кроком step
# range(1, 10, 3) - (1, 4, 7)
# range(1, 10, 2) - (1, 3, 5, 7, 9)

# for змінна in набір_значень:
#     оператори

message = 'Hello'
for i in message:
    print(i)

s = 0
d = 1
for number in range(1, 6):
    s = s + number
    d = d * number
print(s)
print(d)