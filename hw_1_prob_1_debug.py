from __future__ import division, absolute_import
# import math
# import numpy as np

dec_num = int(input("Enter the decimal number you would like to be converted to binary.: "))

pow_of_2 = 1

while dec_num // (2**pow_of_2) != 1:
    pow_of_2 += 1

binary = []
binary.append(1)
bin_text = '1'

largest_pow = pow_of_2
rem_1 = dec_num % (2**pow_of_2)
pow_of_2 -= 1


for pp in reversed(range(pow_of_2+1)):
    print("Rem_1: {0}".format(rem_1))
    print("pp = {0}".format(pp))
    if(rem_1 // (2**pp) == 1):
        print("pp: {0}".format(2**pp))
        print("Mod: {0}".format(rem_1%(2**pp)))
        binary.append(1)
        bin_text += '1'
        rem_1 = rem_1%(2**pp)

    # if(rem_1 // (2**pp) != 1):
    else:
        print("divisor: {0}".format(2**pp))
        binary.append(0)
        bin_text += '0'

final_binary = int(bin_text)
    # else:


    #rem_1 = rem_1 % (pp)





#78%64 = 14
#14%8  = 6
#6%4   = 2
#2%2   = 1


#1001110

#0+2+4+8+64


###########
# Take a number. Figure out the biggest power of 2 it is divisible by
# Find the modulus.
# Repeat procedure



#78/2 = 39
#78/4 = 19, %2
#78/8 = 9, %6
#78/16= 4, %14
#78/32= 2, %14
#78/64= 1, %14

#78/64= 1, %14
#14/32= 0
#14/16= 0
#14/8= 1, %6
#6/4 = 1, %2
#2/2 = 1, %0



#97/2 = 48, %1
#97/4 = 24, %1
#97/8 = 12, %1
#97/16= 6,  %1
#97/32= 3,  %1
#97/64= 1,  %33

#33/32 = 1, %1

#1/16 =  0, %1
#1/8  =  0, %1
#1/4
#1/2
#1/1  = 1, %0

#1100001

##Keep adding to the power of two, until the integer division yields 1
##Take the modulus
############