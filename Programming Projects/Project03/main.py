'''
DEVELOPER: Raul Aguilar
COURSE:	CS226 Discrete Structures
PROJECT:	Project03
LAST MODIFIED: September 29 2021
'''
##########################################
#   Euclidean Algorithm and the Great Common Divisor
##########################################
# PROGRAM DESCRIPTION:
##########################################
# Program takes two positive integers from console input and finds
# their greatest common divisor using the Euclidean Algorithm. Output
# both the greatest common divisor and least common multiple of the two
# integers.
##########################################
# FUNCTIONS:
##########################################
def gcd(inta, intb):
    # Finds the greatest common divisor using the Euclidean algorithm
    remainder = inta%intb
    if remainder == 0:
        return intb

    return gcd(intb, remainder)

def lcm(inta, intb):
    # Finds the least common multiple using the GCD of the integers
    return (inta*intb)//(gcd(inta, intb))

##########################################
# MAIN PROGRAM:
##########################################
def main():
    print("Enter two positive integers")
    a = int(input("a: "))
    b = int(input("b: "))
    s = 'The GCD of ' + repr(a) + ' and ' + repr(b) + ' is ' + repr(gcd(a, b))
    print(s)
    s = 'The LCM of ' + repr(a) + ' and ' + repr(b) + ' is ' + repr(lcm(a, b))
    print(s)

main()