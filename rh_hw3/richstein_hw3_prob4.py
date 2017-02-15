"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 4: Numerical Integral
Last edited: 14 February 2017

Overview:
---------
This program calculates the values of an integral from 0 to 3 in steps of 0.1
using Simpson's method. It then plots the integral as a function of x.

Input:
------
No user input

Output:
-------
A plot, showing the integral as a function of x


"""

from numpy import exp, arange, array
from matplotlib import pyplot as plt

step_size = 0.1  # Calculating the integral for values of x from 0 to 3 in
				 # steps of this size. For example, we'd calculate from 0 to
				 # 0.1, 0.1 to 0.2, 0.2 to 0.3, and so on.
N = 10  # Picking the number of slices to use when calculating the area
		# between one edge of the larger slice and the other. This is the
		# number of steps used in the integration process of a single slice of
		# width 0.1. So, in finding the integral from 0 to 0.1, we break that
		# chunk into 10 slices to use for Simpson's method.

x_arr = arange(0, 3.1, step_size)  # Creating an array to house the edges of
								   # all of the slices; one more edge than
								   # areas calculated


def t_func(x):  # The function being integrated; will be called on a lot
	result = exp(x**2)

	return result


def int_steps(a, b, N):  # Calculating the area of each little slice
	h = (b - a) / N  # Step-size between each of the little steps

	sum_3 = float(0)  # The sum which will be in term 3
	sum_4 = float(0)  # The sum which will be in term 4

	first_term = t_func(a)
	second_term = t_func(b)

	for kk in range(1, N, 2):  # All of the odd terms
		sum_3 += t_func(a + (kk * h))

	third_term = 4 * sum_3

	for kk in range(2, N, 2):  # All of the even terms
		sum_4 += t_func(a + (kk * h))

	fourth_term = 2 * sum_4

	simp_int = (h / 3) * (first_term + second_term + third_term + fourth_term)

	return simp_int

# Will have the areas of each individual slice
little_areas = [[] for xx in range(len(x_arr))]
little_areas[0] = 0  # First value set to zero, because at point zero, there is
					 # no area under the curve

# Going to store the sum of the slice areas here.
int_val_arr = [[] for xx in range(len(x_arr))]
int_val_arr[0] = 0  # Again, first term 0, so zero will be plotted

summ = float(0)

for xx in range(len(x_arr) - 1):  # length minus one because in the indexing,
								  # we beed to call xx + 1
	a = x_arr[xx]  # Setting the lower boundary
	b = x_arr[xx + 1]  # Setting the upper boundary

	little_areas[xx + 1] = int_steps(a, b, N)  # Storing the area calculated
											   # from between the two edges

	summ += little_areas[xx + 1]  # Adding this value to a sum of the full area

	int_val_arr[xx + 1] = summ  # Putting the sum in an array for future plot

int_val_arr = array(int_val_arr)

fig, ax = plt.subplots()
ax.plot(x_arr, int_val_arr, color="purple")
ax.set_xlabel("x-value")
ax.set_ylabel("E(x): Area under the curve up to this point")
ax.set_title("Plot of E(x)")

plt.tight_layout()
plt.show()

# END PROGRAM
