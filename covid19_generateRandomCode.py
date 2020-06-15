import random, string

"""Function generateRandomCode()
@param length: length of alphanumeric code
Description: The sgenerateRandomCode() function takes in one parameter,
             length, which is set to 10. The function then generates
             a random alphanumeric code of that length and returns it.
"""
def generateRandomCode(length=10):

    availableCharacters = string.digits+string.ascii_letters
    return ''.join(random.choice(availableCharacters) for i in range(length))

# print(generateRandomCode())
