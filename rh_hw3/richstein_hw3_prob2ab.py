"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 2a, 2b
Last edited: 12 February 2017

Overview:
---------
This program implements two functions using different equation forms to solve
for the roots of the quadratic equation

Input:
------
The coefficients of the quadratic equation

Output:
-------
The two roots, as found by each function

Program Limitations:
--------------------
Machine precision

"""
from numpy import sqrt, array, sort

a = float(input("Please enter the three coefficients. \na: "))
b = float(input("b: "))
c = float(input("c: "))

###############################################################################
# Function implementing the standard formula for finding the roots of the
# quadratic equation


def quad_func(a, b, c):
	discriminant = sqrt(b**2 - (4 * a * c))

	x_pos_d = discriminant
	x_neg_d = -discriminant

	results = array([x_pos_d, x_neg_d])

	results += (-b)
	results /= (2 * a)

	return sort(results)

###############################################################################
# Function implementing the a different, but equivalent formula for finding the
# roots of the quadratic equation


def sec_q_func(a, b, c):
	numerator = 2 * c
	discriminant = sqrt(b**2 - (4 * a * c))

	plus_denom = -b + discriminant
	neg_denom = -b - discriminant

	results = array([(numerator / plus_denom), (numerator / neg_denom)])

	return sort(results)

###############################################################################
# Calculating the roots and printing them
# Printing all of the digits in order to best see where the roots differ

func_1_res = quad_func(a, b, c)

func_2_res = sec_q_func(a, b, c)

print("\nSolutions, Method 1: ({0}, {1})".format(func_1_res[0],
      func_1_res[1]))

print("\nSolutions, Method 2: ({0}, {1})".format(func_2_res[0], func_2_res[1]))

# END PROGRAM
