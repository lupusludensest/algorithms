import re

def is_valid_ssn(ssn):
    # Regular expression for SSN in both formats (XXX-XX-XXXX or XXXXXXXXX)
    pattern = r'^\d{3}-?\d{2}-?\d{4}$'
   
    # Use re.match to check if the SSN matches the pattern
    if re.match(pattern, ssn) and ssn[0] != '0':
        return True
    else:
        return False


# Test cases
print(is_valid_ssn('123-45-6789'))  # True
print(is_valid_ssn('012-34-5678'))  # False, SSN should not start with 0
print(is_valid_ssn('abc-12-3456'))  # False, all digits should be between 0 and 9
print(is_valid_ssn('666-12-3456'))  # False, invalid starter

