#відкриття файлу w-запису, r - читання, a - для дозапису, b - бінарний файл
# myfile = open('hello.txt', 'w')
# myfile.write('Hello \n')
# myfile.close()

with open('hello.txt', 'a') as somefile:
    somefile.write('Hello from with')

#читання файлу
#readline() - зчитує один рядок
#read() - зчитує весь вміст файлу в один рядок
#readlines() - зчитує всі рядки файлу в список
list_of_elements = []
with open('hello.txt', 'r') as somefile:
    number_of_elements = somefile.readline()
    print(number_of_elements)
    for i in range(1, int(number_of_elements)+1):
        list_of_elements.append(somefile.readline())
print(list_of_elements)

