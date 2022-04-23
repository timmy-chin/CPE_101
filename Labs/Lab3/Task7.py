def upper_or_lower(char):
    if 97 <= ord(char) <= 122:
        return True
    else:
        return False

print(upper_or_lower(input('Enter an Upper or Lowercase Character: ')))