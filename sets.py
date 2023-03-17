#Множина зберігає тільки унікальні елементи
users = {'Igor', 'Kateryna', 'Tetiana', 'Igor'}
print(users)

#Створення множин з списків
students = ['Olena', 'Iryna', 'Serhii']
students_set = set(students)
print(students_set)

#Створення порожньої множини
users = set()

print(len(students_set))

#Додавання елементів в множину
students = {'Olena', 'Iryna', 'Serhii'}
students.add('Mariia')
students.add('Mykola')
print(students)

#Видалення елементу з множини - remove()
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
students.remove('Serhii')
print(students)
if 'Serhii' in students:
    students.remove('Serhii')

#discard() - видаляє елементи з множини (не генерує помилку у випадку відсутності елемента)
students.discard('Serhii')
students.discard('Mariia')
print(students)

#Видаляє всі елементи з множини
students.clear()

#Перебір всіх елементів з множини
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
for stud in students:
    print(stud)

#Операції з множинами
#копіювання
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
users = students.copy()

#Об'єднання множин
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
students_2 = {'Dmytro', 'Yuriy', 'Igor', 'Olena'}
all_students = students.union(students_2)
print(all_students)

#Перетин множин - повертає спільні елементи
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
students_2 = {'Dmytro', 'Yuriy', 'Igor', 'Olena'}
stud_3 = students.intersection(students_2)
print(stud_3)
print(students & students_2)

students.intersection_update(students_2)

#Різниця множин - повертає ті елементи, які є в першій множині, але відсутні в другій
students = {'Olena', 'Iryna', 'Serhii', 'Mariia'}
students_2 = {'Dmytro', 'Yuriy', 'Igor', 'Olena'}
stud_3 = students.difference(students_2)
print(stud_3)
stud_3 = students_2.difference(students)
print(stud_3)
print(students - students_2)

#symmetric_difference() - повертає всі елементи обох множин за виключенням спільних
students_3 = students.symmetric_difference(students_2)
print(students_3)
print(students ^ students_2)

#Відношення між множинами
#issubset() - дозволяє перевірити, чи є поточна множина підмножиною іншої
student = {'Olena', 'Yuriy', 'Iryna', 'Serhii', 'Dmytro', 'Igor', 'Mariia'}
st_1 = {'Olena', 'Yuriy', 'Iryna'}
print(student.issubset(st_1))
print(st_1.issubset(student))

#issuperset() - дозволяє перевірити, чи є поточна множина надмножиною іншої
print(student.issuperset(st_1))
print(st_1.issuperset(student))

#frozen set - множина, яка не може бути змінена
users = frozenset(students)
