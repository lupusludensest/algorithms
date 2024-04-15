def comp(array1, array2):

    try:
        return sorted(i * i for i in array1) == sorted(array2)
    except:
        return False

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19])) # True
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19])) # False