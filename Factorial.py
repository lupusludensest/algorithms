# Введите число и выведите на экран его факториал
import math

n = int(input('Введите число n: '))
# вариант 1 for
if n < 0:
    print(f'Вы точно хотите получить результат гамма-функции? Я нет!')
    quit()
result = 1
for i in range(1, n+1):
    result *= i
print(f'Factorial of {n} = {result}')

# вариант 2 while
result = 1
i = 1
while i < n+1:
    result *= i
    i += 1
print(f'Factorial of {n} = {result}')

# вариант 3 для читеров

print(math.factorial(n))


# сложность if O(1) + for / while O(N) = O(N)
