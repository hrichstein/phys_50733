"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
Homework 4, Problem 2 - Monte Carlo Integration
Last edited: 24 February 2017

Overview:
---------
This script uses the importance sampling formula to calculate the value for an
integral using Monte Carlo integration.

Input:
------
None

Output:
-------
This script will print the value of the final calculated integral.

"""
from numpy import exp, sqrt
from random import random

N = int(1e6) # Number of steps
int_val = 2  # This is the value of the integral of w_x calculated
			 # analytically, but also given in the book.


def p_rand():
	"""

	This function will take the uniformly distributed random
	numbers and transform them to be non-uniformaly distributed
	according to our p(x). See paper for derivation of equation used.

	"""
	rand_val = (random())**2

	return rand_val


int_sum = float(0)

for xx in range(N):  # This will loop N times
	temp = p_rand()  # Need to save the random number for use in importance
					 # sampling formula.
	f_x = (temp**(-1 / 2)) / (exp(temp) + 1)
	w_x = temp**(-1 / 2)

	int_sum += (f_x / w_x)

I = (1 / N) * int_sum * int_val  # Integral using (10.42) from book
								 # Fundamental formula for importance sampling

print(I)

# END PROGRAM
