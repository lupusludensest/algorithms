# Последовательность Фибоначчи определяется так:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# По данному числу n выведите на экран все числа ряда до n-го числа Фибоначчи φn.

# Формула:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2

# n = int(input("Элемент ряда Фибоначчи: "))

# def fibonacci(n):
#     fibonacci1 = 1
#     fibonacci2 = 1
#     print(fibonacci1)
#     print(fibonacci2)
#     i = 0
#     while i < n - 2:
#         fibonacci_sum = fibonacci1 + fibonacci2
#         fibonacci1 = fibonacci2
#         fibonacci2 = fibonacci_sum
#         i = i + 1
#         print(f'{fibonacci2}')
#
# fibonacci(n)

n = int(input("Элемент ряда Фибоначчи: "))
def fibonacci_for(m):
    fibonacci1 = 1
    fibonacci2 = 1
    if m < 1:
        print(f'Неверное значение')
        quit()
    elif m == 1:
        print(fibonacci1)
    else:
        print(fibonacci1)
        print(fibonacci2)
        for i in range(2, m):
            fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
            print(fibonacci2)

fibonacci_for(n)

# Сложность O(N)
# TODO: Домашнее задание: Написать программу для вывода только указаного элемента последовательности