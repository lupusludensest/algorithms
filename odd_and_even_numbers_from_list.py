# Odd and even numbers from list

numbers = [-23, -23, -23, -6, 0, 5, 4, 88]

def odd_and_even_numbers_from_list(numbers):
  """Separates a list of numbers into even and odd number lists.

  Args:
      numbers: A list of integers.

  Returns:
      A tuple containing two lists: even_numbers and odd_numbers.
  """
  even_numbers = []
  odd_numbers = []
  
  for el in list(set(numbers)): # remove duplicates
    if el % 2 == 0:
      even_numbers.append(el)  # Append only even numbers to even_numbers list
    else:
      odd_numbers.append(el)  # Append only odd numbers to odd_numbers list
  
  return even_numbers, odd_numbers

even_numbers, odd_numbers = odd_and_even_numbers_from_list(numbers)
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")