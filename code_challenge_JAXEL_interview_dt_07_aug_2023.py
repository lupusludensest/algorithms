# interview witn JAXEL, Chingis Kiunkrikov and Maksim
# decorators
# context managers
# parametrization
# parallel call one class from another

# https://code.yandex-team.ru/02b4f041-e905-4de7-8d8b-d276b166e9cb
# input: two sorted lists
    # a - sorted list, size n
    # b - sorted list, size m
# output: intersection of two lists a and b
# example:
# a = [1, 3, 4, 5, 7]
# b = [3, 5, 6]
# expected_output = [3, 5]

a = [1, 3, 4, 5, 7]
b = [3, 5, 6]
def sm_fn(a, b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c

print(sm_fn(a, b))
def sm_fn(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
    return c

print(sm_fn(a, b))
