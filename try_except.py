def divide(numerator: float, denominator: float) -> float:
  """Divides two numbers and handles potential ZeroDivisionError.

  Args:
      numerator: The numerator (number to be divided).
      denominator: The denominator (number dividing the numerator).

  Returns:
      The result of the division or None if an error occurs.
  """

  try:
    result = numerator / denominator
    return result
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    return None  # Return None only in case of ZeroDivisionError

print(divide(4.0, 2.0))  # Output: 2.0
print(divide(4.0, 0.0))  # Output: Error: Cannot divide by zero. None
