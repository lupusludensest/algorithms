import re

def is_valid_ssn(ssn):
    # Regular expression for SSN in both formats (XXX-XX-XXXX or XXXXXXXXX)
    pattern = r'^\d{3}-?\d{2}-?\d{4}$' # ^\ - beginning d - digits ? char can be or not can be $ - end

    # Use re.match to check if the SSN matches the pattern
    if re.match(pattern, ssn):
        return True
    else:
        return False

print(is_valid_ssn("714-33-5179"))