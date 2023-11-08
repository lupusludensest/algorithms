# Derivco  https:// (https://derivco.kattis.com/test/programming/ia5mmozc9dbzuw38rwnz6v3yttbksvq5)derivco (https://derivco.kattis.com/test/programming/ia5mmozc9dbzuw38rwnz6v3yttbksvq5).kattis.com/test/programming/ia5mmozc9dbzuw38rwnz6v3yttbksvq5 (https://derivco.kattis.com/test/programming/ia5mmozc9dbzuw38rwnz6v3yttbksvq5)
# 06 nov 2023
# Three non-negative integers, where
# equals the number of empty soda bottles in Tim’s possession at the start of the day,
# the number of empty soda bottles found during the day, and
# the number of empty bottles required to buy a new soda
# Output
# How many sodas did Tim drink on his extra thirsty day?

def maxSodas(e, f, c):
    totalBottles = e + f
    sodasDrunk = totalBottles // c

    remainingBottles = totalBottles % c
    total = sodasDrunk + remainingBottles

    while sodasDrunk >= c:
        additionalSodas = sodasDrunk // c
        remainingBottles = sodasDrunk % c
        total += additionalSodas + remainingBottles
        sodasDrunk = sodasDrunk // c

    return total

initialBottles = 5
foundDuringDay = 4
bottlesRequired = 2

print(maxSodas(initialBottles, foundDuringDay, bottlesRequired))
