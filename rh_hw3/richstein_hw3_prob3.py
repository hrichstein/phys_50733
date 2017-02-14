"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
ASSIGNMENT
Last edited:

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

from numpy import exp
from scipy.constants import k

print(k)

T = float(input("Please enter the temperature in Kelvin: "))

rho = 6.022e28  # m^-3
debye_t = 428  # K
V = 1000  # cm^3 of solid aluminum


def inner_func(x):
	numerator = (x**4) * exp(x)
	denominator = (e**x - 1)**2

	return numerator / denominator


def cv(T):
	a = 0
	b = debye_t / T
	N = 1000
	h = (b - a) / N

	first_term = 0.  # if put into the function, would return NaN
	second_term = (1 / 2) * inner_func(b)

	summ = float(0)

	for nn in range(len(N)) > 0:
		summ += inner_func(a + (k * h))

	integral = h * (first_term + second_term + summ)

	c_v = 9 * V * rho * k * ((T / debye_t)**3) * integral

	return c_v

h_cap = cv(T)

print("The heat capacity is {0}".format(h_cap))
