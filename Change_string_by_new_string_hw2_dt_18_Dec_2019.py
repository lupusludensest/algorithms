string = str(input("Enter the string: "))
print(string)

subStrOld = input("Old substring: ")
subStrNew = input("New substring: ")
lenStrOld = len(subStrOld)

while string.find(subStrOld) > 0:
    i = string.find(subStrOld)
    string = string[:i] + subStrNew + string[i+lenStrOld:]

print(f'Edited string: {string}')