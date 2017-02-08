"""
-------------------------------------------------------------------------------
Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 1, Problem 1
Last edited: 7 Feb 2017

Overview:
---------
This program asks the user for a number in base 10 and returns the base 2
equivalent.

Input:
------
A base 10 integer

Output:
-------
A base 2 integer

Program Limitations:
--------------------
Assumes the user does not put in a negative number

Significant Program Variables:
------------------------------
dec_num: integer-like
    the base 10 integer the user enters

pow_of_2: integer-like
    keeping track of the current power of 2 being used as the divisor

bin_text: string-like
    a string in which I will be keeping track of the 1s and 0s associated with
    the conversion to binary

rem: integer-like
    the modulus of the decimal number after it has been divided by the largest
    power of 2 possible (the integer division yields 1)

final_binary: integer-like
    the binary equivalent of the original dec_num

"""

from __future__ import division, absolute_import

# Asking for user input
dec_num = int(input("Enter the decimal number you would like to be converted "
                  + "to binary: "))

# Beginning with 0, in case the decimal number is just 1
pow_of_2 = 0

# If the number is non-zero
if(dec_num//(2**pow_of_2) != 0):
    bin_text = '1'

    # While integer division by some power of two is not 1, increase the power
    while dec_num // (2**pow_of_2) != 1:
        pow_of_2 += 1

    # After the dec_num has been divded by the largest power of 2 possible, take
    # the modulus
    rem = dec_num % (2**pow_of_2)

    # For each power of 2 less than the largest, see if integer division of the
    # remainder by the new power yields 1. If so, add '1' to the binary string.
    # Then, find the new remaineder. If the number is not divisible by the next
    # largest power of 2, add '0'.
    for pp in reversed(range(pow_of_2)):
        if(rem // (2**pp) == 1):
            bin_text += '1'
            rem = rem % (2**pp)

        else:
            bin_text += '0'

# Else, the number is zero
else:
    bin_text = '0'

# Convert the string into an integer
final_binary = int(bin_text)

# Return the original decimal and the new binary conversion to the screen.
print("\nDecimal: {0}".format(dec_num))
print("Binary: {0}".format(final_binary))

# END PROGRAM

"""
1a)

The process by which I determined the algorithm for converting from decimal to
binary:

Take a number. Figure out the largest power of 2 by which it is divisible.
Do this by adding 1 to the power of 2, until the integer division yields 1.
Find the modulus.
Repeat procedure.

Ex. 1 of algorithm
------------------

78/2 = 39
78/4 = 19, %2
78/8 = 9, %6
78/16= 4, %14
78/32= 2, %14
78/64= 1, %14
===============
78/64= 1, %14
14/32= 0, %14
14/16= 0, %14
14/8 = 1, %6
6/4  = 1, %2
2/2  = 1, %0
0/1  = 0, %0

1001110
64+0+0+8+4+2+0 = 78

Ex. 2 of algorithm
------------------
97/2 = 48, %1
97/4 = 24, %1
97/8 = 12, %1
97/16= 6,  %1
97/32= 3,  %1
97/64= 1,  %33
===============
97/64= 1,  %33
33/32= 1, %1
1/16 = 0, %1
1/8  = 0, %1
1/4  = 0, %1
1/2  = 0, %1
1/1  = 1, %0

1100001
64+32+1 = 97

"""
