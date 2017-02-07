"""
-------------------------------------------------------------------------------
Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
In-Class Exercise, 1 February 2017
Last edited: 6 February 2017

Overview:
---------
This program outputs calculated values for e^(-x) for 0-100 in steps of 10.

Input:
------
N/A

Output:
-------
Calculated values for e^(-x), as well as those same values from numpy's exp(x).

Program Limitations:
--------------------
Machine precision

"""

from numpy import linspace, exp
from math import factorial

#Creating an array to pull x-values from
x_array  = linspace(0,100,11)

#Declaring variables
sum_1    = float(0)
s_n      = 1 #set to a value so the while-loop will initialize
epsilon  = 1e-12

#Summation
for xx in x_array:
    n   = 0
    s_n = 1
    #Keep adding terms by increasing n, until the additive term becomes
    #insignificant in comparison to the machine precision
    while abs(s_n) > epsilon:
        s_n    = ( (xx**n) / (factorial(n)) )
        sum_1 += s_n
        n     += 1
        if n  == 153: #A condition needed, because sometimes n will get too big
                      #before the term becomes insignificant, and there is
                      #overflow. A max value of n had to be put into place, and 
                      #this was the one every value could reach before breaking.
            break

    inverse_sum = 1/sum_1

    print("")
    print("x = {0}".format(xx)) #Print the x-value
    print("Inverse = {0}".format(inverse_sum)) #Print the calculated value
    print("Numpy   = {0:.12e}".format(exp(-xx))) #Print the numpy value

#END PROGRAM

"""
Sample Output
-------------

x = 0.0
Inverse = 1.0
Numpy   = 1.000000000000e+00

x = 10.0
Inverse = 4.53978687024e-05
Numpy   = 4.539992976248e-05

x = 20.0
Inverse = 2.06106004621e-09
Numpy   = 2.061153622439e-09

x = 30.0
Inverse = 9.35719813341e-14
Numpy   = 9.357622968840e-14

x = 40.0
Inverse = 4.24816138031e-18
Numpy   = 4.248354255292e-18

x = 50.0
Inverse = 1.92866228286e-22
Numpy   = 1.928749847964e-22

x = 60.0
Inverse = 8.75611321772e-27
Numpy   = 8.756510762697e-27

x = 70.0
Inverse = 3.97526925077e-31
Numpy   = 3.975449735909e-31

x = 80.0
Inverse = 1.80476944772e-35
Numpy   = 1.804851387845e-35

x = 90.0
Inverse = 8.19364062433e-40
Numpy   = 8.194012623991e-40

x = 100.0
Inverse = 3.71990901242e-44
Numpy   = 3.720075976021e-44
"""








        



#while abs(sum - (sum+s_n)) < epsilon:   