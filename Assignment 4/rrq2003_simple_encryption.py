"""This script asks the user if they want to encrypt or decrypt a message
the user can also change the shift value for the encoding if they input *

Submitted by Reyhan Quayum, rrq2003
"""

import encoder as encode

secret_key = 13
keep_asking = True
invalid_key = False  # keeps track of whether a key value greater than 0 has been input for secret_key
while keep_asking == True:
    choice = input("Would you like to encrypt (E) or decrypt (D)?")
    if choice == "*":
        secret_key = int(input("Give a key value greater than 0"))
        if secret_key <= 0:
            invalid_key = True
        else:
            invalid_key = False
        while invalid_key == True:
            secret_key = int(input("Give a key value greater than 0"))
            if secret_key <= 0:
                invalid_key = True
            else:
                invalid_key = False
    if choice == "E" or choice == "e":
        message = input("What message would you like to encrypt?")
        print(encode.encrypt(message, secret_key))
    if choice == "D" or choice == "d":
        message = input("What message would you like to decrypt?")
        print(encode.decrypt(message, secret_key))
    if choice == "":  # terminates loop if user presses enter
        keep_asking = False
