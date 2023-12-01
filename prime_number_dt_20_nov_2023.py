# Your function should take a single integer as input.
# It should return true if the number is a prime, and false otherwise.
# Prime is an integer that can be divided by itself and 1 and min prime is 2
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

n = int(input('Enter prime: '))

def if_pr(n):
    if n < 2:
        return False
    for el in range(2, n):
        if n % el == 0:
            return False
    return True

print(if_pr(n))

n = int(input('Enter the prime to evaluate: '))

def if_prm(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return f"Not a prime"
    else:
        return f'The prime'

print(if_prm(n))
