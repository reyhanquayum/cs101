"""This script asks the user for a number in base 10 to convert to another base by using a while loop to concatenate
to a result string by repeatedly dividing the base 10 number by the given base until there is no remainder to get the
number of loops.

Submitted by Reyhan Quayum, NetID rrq2003
"""

num = int(input("What number are you interested in converting?"))
base = int(input("What base shall I use?"))
temp = num
resultbuilder = str()
foundresult = False  # control variable
while foundresult == False:
    if base >= 2 and base <= 9:
        if temp != 0:  # loop stops running once number can no longer be divided
            resultbuilder += str(temp % base)  # looped concatenation to string result with each remainder
            temp = temp//base
        else:
            reversedresult = resultbuilder[
                             ::-1]  # string needs to be reversed because the result is built in opposite direction
            print(f"The number {num}, is represented by {reversedresult} in base {base}.")
            foundresult = True
    else:
        print("The base has to be between 2 and 9. Please try again.")
        foundresult = True
