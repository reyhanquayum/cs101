"""Utilities for encrypting and decrypting using RSA


Prepared by Mauricio Arias

Basic functions for illustration purpose. Functions included:
gcd() calculates the Greatest Common Divisor
coefficients() gets the coefficients in the extended Euclidean
algorithm.
get_private_key uses Euler's tot formula and the Euclidean
algorithm to calculate a private key.
"""


import math

def coefficients(num1, num2, s0=1, t0=0, s1=0, t1=1):
    """This function returns the coefficients for the gcd equation."""
    quotient = num1 // num2
    residue = num1 % num2
    # This method is based on the extended Euclidean algorithm.
    new_s = s0 - quotient * s1
    new_t = t0 - quotient * t1
    if num2 % residue == 0:
        # The coefficients are reported as a tuple.
        return (new_s, new_t)
    else:
        # Recursion is used to simplify the function
        return coefficients(num2, residue, s1 ,t1 ,new_s, new_t)

def gcd(num1, num2):
    """The GCD using the Euclidean Algorithm.""" 
    residue = num1 % num2
    if residue == 0:
        return num2
    else:
        # Using recursion to simplify the function
        return gcd(num2, residue)

def raise_mod(base, exp, mod):
    if (base < 0 or not(isinstance(base,int)) or exp < 0 or not(isinstance(exp, int)) or mod < 0 or
            not(isinstance(mod, int))):
        return 0  # return 0 if 3 positive integers are not input
    foundresult = False
    temp = exp
    resultbuilder = str()
    while foundresult == False:
        if temp > 0:
            resultbuilder += str(temp % 2)
            temp = temp // 2
        else:
            foundresult = True
    prod = 1
    factor = base
    for character in resultbuilder:
        if character == "1":
            prod = (prod * factor) % mod
        factor = (factor ** 2) % mod
    return prod

def get_private_key(p1, p2, p3):
    """Calculation of the private key using the minimal cycler number"""
    max_allowed = math.log(p1 * p2)/math.log(2)
    print(f"The max number that can be encrypted is {p1 * p2 - 1}")
    print(f"It corresponds to {int(math.log(p1*p2)/math.log(2))} bits")

    # Using a modified Euler's formula
    minimal_cycler = (p1-1)*(p2-1) // gcd(p1-1, p2-1)

    # The first coefficient from the extended Euclidean algorithm is
    # the private key.
    coeff1, coeff2 = coefficients(p3, minimal_cycler)
    # The modulus avoids negative numbers
    return coeff1 % minimal_cycler


