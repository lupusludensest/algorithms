def unique_characters(input_string):
    # Use a dictionary to count occurrences of each character
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Filter characters that occur only once
    unique_chars = [char for char, count in char_count.items() if count == 1]

    # Join and return the unique characters as a string
    return ''.join(unique_chars), type(char_count)


# Example input
input_string = "abccdefe"

# Get unique characters
output_string = unique_characters(input_string)
print(output_string)  # expected output: abdf
