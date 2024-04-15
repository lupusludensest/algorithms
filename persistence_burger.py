def persistence(n):
    if n < 10:
        return 0
    elif n > 9:
        count = 0
    while n > 9:
        product = 1
        for i in str(n):
            product *= int(i)
        n = product
        count += 1

    return count

# Example usage
print(persistence(39))  # Output: 3
print(persistence(999))  # Output: 4
print(persistence(4))   # Output: 0
