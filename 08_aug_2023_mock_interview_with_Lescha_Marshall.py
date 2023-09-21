# 08 aug 2023 mock interview with Lescha Marshall
# SELECT CustomerName, EmployeeID, OrderDate FROM Customers JOIN Orders ON Customers.CustomerId = Orders.CustomerId  WHERE EmployeeID = '5';
#
# SELECT CustomerName, COUNT(*) FROM Customers JOIN Orders ON Customers.CustomerId = Orders.CustomerId  WHERE EmployeeID = '5' GROUP BY CustomerName;
#
# SELECT CustomerName, COUNT(*) FROM Customers JOIN Orders ON Customers.CustomerId = Orders.CustomerId  WHERE EmployeeID = '5' GROUP BY CustomerName HAVING COUNT(*) >= 2;

# Дано число представленное в виде массива
# Например [1,2,3]		равносильно числу 123
# Необходимо вернуть число 124, представленное в виде массива [1, 2, 4]
# То есть при вводе массива из цифр 4, 3,2, 1 он должен вернуть массив из чисел 4,3,2,2
# А при подаче массива из чисел 1,2,3,9 вернуть массив из чисел 1,2,4,0

ints = [1, 2, 3]
ints_1 = [4, 3, 2, 1]
ints_2 = [1, 2, 3, 9]

def add_one(a):
    result = 0
    multiplier = 1
    for i in a[::-1]:
        result += i * multiplier
        multiplier *= 10

        number = result + 1
        digits = []
        num_digits = len(str(number))
        for i in range(num_digits):
            digit = number // 10 ** i % 10
            digits.append(digit)

    return digits[::-1]

print(add_one(ints), add_one(ints_1), add_one(ints_2))
