## with count

# def first_unrepeated_char(s):
#     for char in s:
#         if s.count(char) == 1:
#             return char
#     return None

# print(first_unrepeated_char("swiss"))  # w

## with dictionary

def first_unrepeated_char(s):
    counts = {}

    # Count occurrences
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # Find first character with count 1
    for char in s:
        if counts[char] == 1:
            return f"First unrepeated character in '{s}': {char}, {counts}"

    return None


print(first_unrepeated_char("swiss"))  # w