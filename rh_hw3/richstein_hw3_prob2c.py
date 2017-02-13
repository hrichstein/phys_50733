"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 2c
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


def new_quad(a, b, c):
	disc_1 = b**2
	disc_2 = 4 * a * c
	disc_3 = disc_1 - disc_2
	disc_4 = sqrt(disc_3)

	# first_term = -b / (2 * a)

	# sec_term = disc_4 / (2 * a)

	# results = array([(first_term + sec_term), (first_term - sec_term)])

	# return sort(results)

	# pos_d_num = -b + disc_4
	# neg_d_num = -b - disc_4

	# denom = 2 * a

	# results = array([(pos_d_num / denom), (neg_d_num / denom)])

	# return sort(results)

	# num = 2 * c
	# pos_d_num =

	# first_term = -b / (2 * c)

	# sec_term = disc_4 / (2 * c)

	# results = array([1 / (first_term + sec_term), 1 / (first_term - sec_term)])

	large_root = (-b - disc_4) / (2 * a)
	small_root = (c / a) / large_root

	results = array([large_root, small_root])

	return sort(results)


results_test = array(new_quad(a, b, c))

print("\nSolutions, Method 3: ({0}, {1})".format(results_test[0],
      results_test[1]))
