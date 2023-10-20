# 20 sep 2023, wed. Practice for Disney Python interview

str_a = 'Hello, dude'
print(str_a, type(str_a))

int_a = 123
print(int_a, type(int_a))

flt_a = 123.123
print(flt_a, type(flt_a))

false_a = str_a == int_a
print(false_a, type(false_a))

true_a = str_a == 'Hello, dude'
print(true_a, type(true_a))

lst_a = [1, 'one', 123.123, str_a == int_a]
print(lst_a, type(lst_a))

tuple_a = tuple(lst_a)
print(tuple_a, type(tuple_a))

dict_a = {"id": 1, "name": "vic", "age": 24}
print(dict_a, type(dict_a))

set_a = set(dict_a)
print(set_a, type(set_a))

concatenation_a = str_a + ' ' + "Concatenation"
print(concatenation_a)

for i in range(-2, 2):
    print(i, end = '; ')

print('\n')

for n in range(8, -8, -1):
    print(n, end = '; ')

print('\n')

i = 0
while i < 10:
    i += 1
    print(i, end = '; ')

print('\n')

def foo(n, m):
    return n ** m

print(foo(2, 2))

class employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." + self.lastname + "@gmail.com"

    def giveRaise(self, salary):
        self.salary = salary

class developer(employee):
    def __init__(self, firstname, lastname, salary, programming_language):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = programming_language

    def addLanguage(self, lang):
        self.prog_langs += [lang]

emploee1 = employee("John", "Smith", 80000)

print(emploee1.salary, emploee1.email)

emploee1.giveRaise(100000)

print(emploee1.salary, emploee1.email)

dev1 = developer("Joe", "Montana", 110000, ["Python", "C"])

print(dev1.salary, dev1.email)

dev1.giveRaise(125000)

print(dev1.salary, dev1.email)

dev1.addLanguage("Java")

print(dev1.prog_langs)
