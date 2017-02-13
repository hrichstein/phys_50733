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
from numpy import sqrt, array, sort, around

a = float(input("Please enter the three coefficients. \na: "))
b = float(input("b: "))
c = float(input("c: "))


def new_quad(a, b, c):
	disc_1 = b**2
	disc_2 = 4 * a * c
	disc_3 = disc_1 - disc_2
	disc_4 = sqrt(disc_3)

	discrim = sqrt(b**2 - (4 * a * c))

	print("multi-step = {0}".format(disc_4))
	print("single = {0}".format(discrim))

	pos_d_num = -b + disc_4
	neg_d_num = -b - disc_4

	numers = array([pos_d_num, neg_d_num])
	denom = 2 * a

	for nn in range(len(numers)):
		if (abs(numers[nn]) < 1) and (abs(denom) < 0.1):
			replace = (2 * c) / neg_d_num
			numers[nn] = replace
		else:
			numers[nn] /= denom

	return sort(numers)


results_test = array(new_quad(a, b, c))

print("\nSolutions, Method 3: ({0:.2e}, {1:.2e})".format(results_test[0],
      results_test[1]))
