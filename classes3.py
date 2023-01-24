class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("John","Doe",36)
print(person1.firstName)
print(person1.lastName)
print(person1.age)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary

class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
ahmet = Worker()
ahmet.age

mehmet = Customer()
mehmet.creditCardNumber