def convert(number):
    return bin(number)[2:], oct(number)[2:], hex(number)[2:]

print(convert(-24))