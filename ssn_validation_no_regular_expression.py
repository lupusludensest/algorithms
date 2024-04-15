import re

def validate_ssn(ssn):
    """
    Validate a US Social Security Number (SSN)

    :param ssn: The SSN to validate
    :return: True if the SSN is valid, False otherwise
    """
    # SSN should be a string of 9 digits
    if not isinstance(ssn, str) or len(ssn) != 9:
        return False

    # All digits should be between 0 and 9
    if not all(char.isdigit() for char in ssn):
        return False

    # SSN should not start with certain numbers (according to SSA guidelines)
    invalid_starters = ['000', '666', '900-999']
    if any(ssn.startswith(starter) for starter in invalid_starters):
        return False

    return True

# Test cases
print(validate_ssn('123456789'))  # True
print(validate_ssn('0123456789')) # False, SSN should be 9 digits
print(validate_ssn('abc123456'))  # False, all digits should be between 0 and 9
print(validate_ssn('666123456'))  # False, invalid starter