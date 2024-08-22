class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years"

    def __repr__(self):
        return f"Person(name = {self.name}, age = {self.age})"
    # overriding methods, a string representation of what stores and a textual representation of how the object is made

#instantiating object

person_1 = Person("Alice", 24)
person_2 = Person("Bob", 30)


#calling the overrode methods
print(person_1.__str__()) # Alice, 24 years
print(person_1.__repr__()) # Person(name = Alice, age = 24)

print(person_2.__str__()) # Bob, 30 years
print(person_2.__repr__()) # Person(name = Bob, age = 30)
