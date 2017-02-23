"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
Homework 4, Problem 2 - Monte Carlo Integration
Last edited: 22 February 2017

Overview:
---------


Input:
------


Output:
-------


"""
from numpy import exp, sqrt
from random import random

N = 1e6

# Use transformation method (p. 459)
# Generate random numbers and put them into p_rand to get proper distribution

# then, use those numbers in the summation

def p_rand():
	# test_val = 1/(sqrt(2) * random())
	# return test_val
	test_val = (random())**2

	return test_val


int_sum = float(0)
for xx in range(1,int(N+1)):
	temp = p_rand()
	f_x = (temp**(-1/2)) / (exp(temp) + 1)
	w_x = temp**(-1/2)
	int_sum += ((f_x / w_x) * 2)

I = (1/N) * int_sum

print(I)	