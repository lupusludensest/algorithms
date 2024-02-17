# yield

def my_func():
    return 'Hello'
    return 'my'
    return 'friend'


x = my_func()

for i in x:
    print(i)

print(' ' * 14)


# return

def my_func():
    yield 'Hello'
    yield 'my'
    yield 'friend'


x = my_func()

for i in x:
    print(i)