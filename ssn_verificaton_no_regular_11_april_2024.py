def validate_ssn(ssn):
    # Remove dashes from the SSN
    ssn = ssn.replace("-", "")

    # Check if the SSN has exactly 9 digits
    if len(ssn) != 9:
        return False

    # Check if all characters in the SSN are digits
    if not ssn.isdigit():
        return False

    # Check if the first three digits are within the valid range (001-772)
    first_three_digits = int(ssn[:3])
    if not (1 <= first_three_digits <= 772):
        return False

    # Check if the second two digits are within the valid range (01-99)
    second_two_digits = int(ssn[3:5])
    if not (1 <= second_two_digits <= 99):
        return False

    # Check if the last four digits are within the valid range (0001-9999)
    last_four_digits = int(ssn[5:])
    if not (1 <= last_four_digits <= 9999):
        return False

    # All validation checks passed, SSN is valid
    return True

# Example usage
ssn = "123-45-6789"
if validate_ssn(ssn):
    print(f"{ssn} is a valid SSN.")
else:
    print(f"{ssn} is not a valid SSN.")
