# class клас_нащадок (батьківський_клас):
#       методи та атрибути класу нащадка
from oop import Person

class Employee(Person):
    def work(self):
        print(f'{self.name} працює')

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def display_info(self):
        print(f'Employee {self.name} works in the company {self.company}')
        super().display_info()

kate = Employee('Kate', 27, 'Ukraine')
kate.work()
kate.display_info()

#Множинне успадкування
class Employee_1 ():
    def work(self):
        print(f'{self.name} працює')

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __my_method(self):
        pass

class Student():

    def __init__(self, name, lst_food_like, lst_food_hate):
        self.__name = name
        self.lst_food_like = lst_food_like
        self.lst_food_hate = lst_food_hate

    def taste(self, food_name):
        if food_name in self.lst_food_like:
            return f"{self.name} eats the {food_name} and loves it!"

class OnesThreesNines():
    def __init__(self, number):
        self.__number = number

    @property
    def ones(self):
        return self.__number


n1 = OnesThreesNines()
print(n1.ones)
print(n1.ones_1())

my_stud = Student('igor', ['apple'], ['orange'])
print(my_stud.lst_food_like)
print(my_stud.taste('apple'))
# class WorkingStudent(Employee_1, Student):
#     def fjf(self):

#
# ted = WorkingStudent('Ted')
# ted.work()
# ted.study()


