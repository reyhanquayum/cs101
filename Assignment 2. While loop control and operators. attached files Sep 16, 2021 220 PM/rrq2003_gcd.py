"""This script asks for two numbers and prints the greatest common divisor by using the 
Euclidean algorithm to repeatedly take the mod of the first number by the second number
until there is no remainder, after which the greatest common divisor has been found.

Submitted by Reyhan Quayum, NETID rrq2003
"""

firstnumber = int(input("What is the first number?"))
firstinput = firstnumber
secondnumber = int(input("What is the second number?"))
secondinput = secondnumber
while firstnumber % secondnumber != 0:
    thirdnumber = firstnumber % secondnumber
    firstnumber = secondnumber
    secondnumber = thirdnumber  #thirdnumber acts as a temporary variable to store value

print(f"gcd({firstinput}, {secondinput}) = {secondnumber}")