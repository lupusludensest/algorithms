def xo(s):

    o_c = []
    x_c = []

    for i in s:
        if i.lower() == 'o':
            o_c.append(i)
        elif i.lower() == 'x':
            x_c.append(i)

    if len(o_c) == len(x_c):
        return True, o_c, x_c
    elif len(o_c) != len(x_c):
        return False, o_c, x_c

print(xo("ooxx")) # True
print(xo("zzoo")) # False
print(xo("ooxXm")) # True
