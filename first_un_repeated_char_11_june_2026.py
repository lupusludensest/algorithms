## with count

# def first_unrepeated_char(s):
#     for char in s:
#         if s.count(char) == 1:
#             return char
#     return None

# print(first_unrepeated_char("swiss"))  # w

# with dictionary

def first_unrepeated_char(s):  # s is the input string
    counts = {}  # create an empty dictionary

    # Count occurrences of each character
    for char in s:  # iterate through every character in the string
        if char in counts:  # if the character already exists as a key
            counts[char] += 1  # increment its count
        else:
            counts[char] = 1  # first occurrence of this character

    # Find the first character that appears only once
    for i, char in enumerate(s):  # iterate with index to preserve order
        if counts[char] == 1:  # check its count in the dictionary
            return f"First unrepeated character in '{s}': '{char}' at index {i}, Character counts: {counts}"

    return None  # no unrepeated character exists

n = str(input("Enter the string: "))
print(first_unrepeated_char(n))

