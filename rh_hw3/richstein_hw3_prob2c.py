"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 2c
Last edited: 12 February 2017

Overview:
---------
This is a program which should accurately calculate both roots of a quadratic
equation. It tries to account for issues with machine precision.

Input:
------
The three coefficients of the quadratic equation to be solved.

Output:
-------
The two roots of the quadratic equation, in scientific notation with 2 decimal
places

Program Limitations:
--------------------
Machine precision

"""
from numpy import sqrt, array, sort, around

a = float(input("Please enter the three coefficients. \na: "))
b = float(input("b: "))
c = float(input("c: "))


def new_quad(a, b, c):
	# Had the discriminant calculation broken into several steps, but checked,
	# and the precision was the same
	discrim = sqrt(b**2 - (4 * a * c))

	pos_d_num = -b + discrim  # Adding the discriminant
	neg_d_num = -b - discrim  # Subtracting the discriminant
	denom = 2 * a

	numers = array([pos_d_num, neg_d_num])

	# Checking to see whether I will be dividing a very small number by another
	# small number

	for nn in range(len(numers)):
		if (abs(numers[nn]) < 0.1) and (abs(denom) < 1):
			# If this is true, it will use the other equation to calculate the
			# root instead
			replace = (2 * c) / numers[nn - 1]
			numers[nn] = replace
			# If not true, will simply divide by the normal denominator, 2*a
		else:
			numers[nn] /= denom

	return sort(numers)  # Going to return the roots from more negative to less
						 # less negative


results = new_quad(a, b, c)

print("\nSolutions, Method 3: ({0:.2e}, {1:.2e})".format(results[0],
      results[1]))

# END PROGRAM
