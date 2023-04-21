#Визначення класу
#class назва_класу:
#   атрибути_класу
#   методи_класу

class Person:

    description = "Опис людини"
    type = "Person"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            self.__age = 1

    @property
    def name(self):
        return self.__name

    def say_hello(self):
        self.say("Hello")

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def say(self, message):
        print(message)

    def display_info(self):
        print(f'Name: {self.name} age: {self.__age}')

    def __str__(self):
        return f'Name: {self.name} age: {self.__age}'

    @staticmethod
    def print_type():
        print(Person.type)

ivan = Person('Ivan', 133)
ivan.display_info()

print(ivan.description)
tetiana = Person('Tetiana', 33)
tetiana.display_info()
# ivan.set_age(-133)
ivan.age = -133
ivan.display_info()
print(ivan)
