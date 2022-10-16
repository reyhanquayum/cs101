"""This script does basic RSA encryption and decryption by asking the user for two different large
prime numbers. A private key is generated using the function from the utilities file
and a public key is already pre-defined.

Submitted by Reyhan Quayum, rrq2003
"""

import rrq2003_utilities_RSA as utilities

skip = False
while skip == False:
    public_key = (2 ** 8) + 1  # small prime number AKA public key
    p1 = input("Give one large prime number")
    p2 = input("Give another large prime number")
    message = input("What message would you like to encrypt?")
    if p1 == "" or p2 == "" or message == "":
        skip = True
        break
    p1 = int(p1)
    p2 = int(p2)
    message = int(message)
    n = p1 * p2
    private_key = utilities.get_private_key(p1, p2, public_key)
    cipher = utilities.raise_mod(message, public_key, n)
    decrypted = utilities.raise_mod(cipher, private_key, n)
    print("Your encrypted message is", cipher)
    print("Decrypting the above message yields:", decrypted)
