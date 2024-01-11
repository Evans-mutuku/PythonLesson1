# Python Classes

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def greet(self):
        return f"Hello, my name is {self.name} and my age is {self.age} my gender is {self.gender}"


person1 = Person("John", 22, "Male")

print(person1.greet())


# person = person.Person("sdknsd", 34)