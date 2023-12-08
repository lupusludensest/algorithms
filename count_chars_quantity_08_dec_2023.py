# We have a string give. We need to count each char in the string. And return a string where 'a2b3'.

a = str(input('Enter the string: ')) # abc
def count_chars(a):
    res = ""
    prev_char = ""
    char_count = 0

    for char in a:
        if char != prev_char:
            if len(prev_char) > 0:
                res += prev_char + str(char_count)
            char_count = 1
            prev_char = char
        else:
            char_count += 1

    res += prev_char + str(char_count)
    return res

print(count_chars(a))