import random
import string

def encryptionKeyGenerator(keyLength):

    """This function takes in the desired length of the encryption key
    from the user and generates a random encryption key.
    """
    
    integerLength = int(keyLenght)

    # All character that will be used in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(integerLength))

    print("Your key is: ", password)

keyLenght = input("How many characters would you like your password to have? ")

encryptionKeyGenerator(keyLenght)

