import random

def generate_phone_number():
  """Generates a random phone number in the format (XXX)-XXX-XXXX.

  Returns:
      A string representing a phone number in (XXX)-XXX-XXXX format.
  """

  # Generate random digits for each part of the phone number
  area_code = random.randint(100, 999)
  exchange = random.randint(100, 999)
  subscriber_number = random.randint(1000, 9999)

  # Format the phone number with parentheses and hyphens
  return f"({area_code})-{exchange}-{subscriber_number}"

# Generate and print a sample phone number
phone_number = generate_phone_number()
print(phone_number)
