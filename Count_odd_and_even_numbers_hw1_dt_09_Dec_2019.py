# Посчитать четные и нечетные цифры числа.
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input("Enter the number: "))
even = odd = 0
if n < 0:
    print("Enter positive integer.")
    quit()
elif n == 0:
    print("Zero is neither positive nor negative, and has no sign.")
    quit()
while n > 0:
    if n % 2 == 0:
        even += 1
    elif n % 2 != 0:
        odd += 1
    n = n//10
print("Even: %d, odd: %d" % (even, odd), '.')
print("Even: {}, odd: {}".format(even, odd), '.')
print(f'Even: {even}, odd: {odd}.')