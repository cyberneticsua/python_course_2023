# num = "5"
# number = int(num)
# print(number)
#

# try:
#     наш код
# except [Тип_винятку]:
#     наш код
# Exception -
# IndexError -
# KeyError -
# ZeroDivisionError -
# try:
#     num1 = int(input("Input a number:"))
#     num2 = int(input("Input a number:"))
#     print(f'Результат {num1/num2}')
# except ValueError:
#     print("Перетворення числа не вдалося")
# except ZeroDivisionError:
#     print('Спроба ділення на 0')
# except BaseException:
#     print('Загальна помилка')
# finally:
#     print("Блок try завершився")
# print("Кінець програми")
#
# try:
#     num1 = int(input("Input a number:"))
#     num2 = int(input("Input a number:"))
#     print(f'Результат {num1/num2}')
# except (ValueError, ZeroDivisionError):
#     print("Введено некоректні дані")
# except BaseException:
#     print('Загальна помилка')
# finally:
#     print("Блок try завершився")
#

try:
    num1 = int(input("Input a number:"))
    num2 = int(input("Input a number:"))
    if num2==0:
        raise Exception('Друге число не повинне дорівнювати 0')
    print(f'Результат {num1/num2}')
except ValueError as e:
    print(f"Введено некоректні дані {e}")
except Exception as e:
    print('Загальна помилка', e)
else:
    print('Все пройшло успішно')
finally:
    print("Блок try завершився")

