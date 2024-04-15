def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo("ooxx")) # True
print(xo("zzoo")) # False
print(xo("ooxXm")) # True