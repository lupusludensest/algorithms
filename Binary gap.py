# Найти наибольший пробел в двоичном числе, полученным из
# целочисленного положительного числа в десятичной системе, вводимого пользователем.
# Binary gap - это наибольшая последовательность нулей в двоичном числе,
# начинающемся и заканчивающемся на 1.
# Например 9 в двоичном исчислении это 1001. Максимальная (в данном примере и единственная)
# последовательность идущих подряд нулей равна 2.
# Для числа 529 двоичный аналог выглядит как 1000010001.
# Максимальный разрыв 4 нуля, идущих подряд

n = int(input(f'Введите число: '))
decimal = n
# Получаем число в двоичном представлении
bin_string = ''
while n > 0:
    bin_string += str(n % 2)
    n = n // 2
bin_string = bin_string[::-1]
# print(f'Decimal: {decimal} = Binary: {bin_string}')
#
# Проверяем что разрыв есть и находим его длину
max_gap = 0
counter = 0
bin_gap = False
for char in bin_string:
    if char == '1':
        if max_gap < counter:
            max_gap = counter
        counter = 0
        bin_gap = True
    elif bin_gap:
        counter += 1
print(f'Decimal: {decimal} = Binary: {bin_string}, max gap is: {max_gap}')

# вариант для читеров
bin_str = str(bin(n))
print(f'{str(bin(n))}')
# сложность O(N)
max_gap = 0
counter = 0
bin_gap = False
for x in bin_str:
    if x == '1':
        if max_gap < counter:
            max_gap = counter
        counter = 0
        bin_gap = True
    elif bin_gap:
        counter += 1
print(f'Decimal: {n} = Binary: {bin_str[2:]}, max gap is: {max_gap}')