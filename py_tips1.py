class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." + self.lastname + "@kite.com"

    def giveRaise(self, salary):

        self.salary = salary

class Developer(Employee):

    def __init__(self, firstname, lastname, salary, programming_languages):
        super().__init__(firstname, lastname, salary)
        self.prog_languages = programming_languages

    def addLanguage(self, lang):
        self.prog_languages += [lang]

employee1 = Employee('John', 'Smith', 80000)

print(employee1.salary)

employee1.giveRaise(100000)

print(employee1.salary)

dev1 = Developer('Joe', 'Montana', 100000, ['Python', 'JS'])

print(dev1.salary)

dev1.giveRaise(125000)

print(dev1.salary)

dev1.addLanguage('Ruby')

print(dev1.prog_languages)