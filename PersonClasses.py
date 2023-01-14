class Person:
    def __init__(self, Firstname, LastName, age):
        self.firstname = Firstname
        self.lastname = LastName
        self.age = age

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def isAdult(self):
        return self.age >= 18

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old."

    def __repr__(self):
        return f"Person('{self.firstname}', '{self.lastname}', {self.age})"

p1 = Person("John", "Smith", 35)
print(p1.fullname())
print(p1.isAdult())
print(p1)
print(p1.__repr__())
print(p1.__str__())
print(repr(p1))
print(str(p1))
