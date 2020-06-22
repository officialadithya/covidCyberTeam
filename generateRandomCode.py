import random, string

"""Function generateRandomCode()
@param length: length of alphanumeric code
Description: The generateRandomCode() function takes in one parameter,
             length, which is set to 10. The function then generates
             a random alphanumeric code of that length and returns it.
"""
def generateRandomCode(usedCodes, length=10):

    availableCharacters = string.digits+string.ascii_letters
    with open("usedCodes.txt","a") as usedCodes:
        code = ''.join(random.choice(availableCharacters) for i in range(length))
        return code
usedCodes = []
usedCodes.append(generateRandomCode(usedCodes))
