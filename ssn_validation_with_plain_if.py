def validate_ssn(ssn):
    ssn_ready = str(int(ssn.replace('-', '').replace(' ', '')))

    if len(ssn_ready) == 9 and ssn_ready[0] != '0':
        return True
    else:
        return False

print(validate_ssn('114-33-5175  ')) # True
print(validate_ssn('14-33-517  ')) # False
print(validate_ssn('a14-33-5175  ')) # ValueError: invalid literal for int() with base 10: 'a14335175'