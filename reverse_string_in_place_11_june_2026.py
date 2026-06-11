def reverse_string_in_place(s):
    s = list(s)
    # s must be a mutable sequence (e.g., a list of characters)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)


s =str(input("Enter the string: "))
print(reverse_string_in_place(s))