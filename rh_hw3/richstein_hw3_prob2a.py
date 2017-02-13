"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 2a
Last edited: 12 February 2017

Overview:
---------


Input:
------


Output:
-------


Program Limitations:
--------------------


Significant Program Variables:
------------------------------


"""
from numpy import sqrt, array, sort

a = float(input("Please enter the three coefficients. \na: "))
b = float(input("b: "))
c = float(input("c: "))


def quad_func(a, b, c):
	discriminant = sqrt(b**2 - (4*a*c))

	x_pos_d = discriminant
	x_neg_d = -discriminant

	results = array([x_pos_d, x_neg_d])

	results += (-b)
	results /= (2*a)

	return sort(results)


results_test = array(quad_func(a, b, c))

print("\nSolutions: ({0}, {1})".format(results_test[0], results_test[1]))
