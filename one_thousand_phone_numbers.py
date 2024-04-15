import random
import string

def generate_phone_number():
    area_code = str(random.randint(100, 999))
    prefix = str(random.randint(100, 999))
    line_number = str(random.randint(1000, 9999))
    return f"{area_code}-{prefix}-{line_number}"

phone_numbers = set()
while len(phone_numbers) < 1000:
    phone_number = generate_phone_number()
    phone_numbers.add(phone_number)

print(phone_numbers)