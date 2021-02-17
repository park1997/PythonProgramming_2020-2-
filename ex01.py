def in_acceptable_range(number):
    if (number<10**(7) and number >10**(-7)) or ((-number) > 10**(-7) and (-number) < 10**7):
        return True
    return False

print(in_acceptable_range(10))