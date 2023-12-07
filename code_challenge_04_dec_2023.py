# ещё одна задачка, с которой во время интервью я бы не справился: надо сдвинуть все нули в листе направо,
# не создавая промежуточных копий, — всё на месте

def sort_zeros(arr):
    """
    Moves all zeros in the array to the end, while maintaining the order of non-zero elements.
    The operation is done in-place.

    :param arr: List of integers, which may contain zeros.
    """
    # Initialize a pointer to keep track of the position for non-zero elements
    position = 0

    # Iterate over the array
    for i in range(len(arr)):
        # If the current element is not zero, swap it with the element at the 'position'
        if arr[i] != 0:
            arr[i], arr[position] = arr[position], arr[i]
            position += 1

    return arr

# Example usage
example_array = [1, 0, 3, 0, 0, 4]
print(sort_zeros(example_array))

# Expected output for that input: [1, 3, 4, 0, 0, 0]