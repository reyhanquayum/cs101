"""This module defines two functions for encryption and decryption through the use of
the index of list alphabet

Submitted by Reyhan Quayum, rrq2003
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ".", ",", ":", ";", "!", "?", "-", "&", "(", ")",
            "#"]


def encrypt(userinput: str, shift: int):
    encrypted_message = ""
    for character in userinput:
        if alphabet.index(character) + shift < len(alphabet):
            shifted_index = (alphabet.index(character) + shift)
            encrypted_message = encrypted_message + alphabet[shifted_index]
        elif alphabet.index(character) + shift >= len(alphabet):
            # subtract length of alphabet from index to allow looping around the list
            shifted_index = (alphabet.index(character) - len(alphabet)) + shift
            encrypted_message = encrypted_message + alphabet[shifted_index]
    return encrypted_message


def decrypt(userinput: str, shift: int):
    decrypted_message = ""
    shift = -shift
    for character in userinput:
        if alphabet.index(character) + shift < len(alphabet):
            shifted_index = (alphabet.index(character) + shift)
            decrypted_message = decrypted_message + alphabet[shifted_index]
        # if the the shift value causes the index to go outside alphabet's range
        elif alphabet.index(character) + shift >= len(alphabet):
            # subtract length of alphabet from index to allow looping around the list
            shifted_index = (alphabet.index(character) - len(alphabet)) + shift
            decrypted_message = decrypted_message + alphabet[shifted_index]
    return decrypted_message


