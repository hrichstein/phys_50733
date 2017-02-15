"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 3
Last edited: 14 February 2017

Overview:
---------


Input:
------


Output:
-------


Program Limitations:
--------------------


"""

from numpy import exp, linspace

a = 0
b = 3
h = 0.1  # stepsize

val_arr = linspace(a, b, h)

# N = 100

N = int(input("N: "))


def t_func(x):
	result = exp(x**2)

	return result


first_term = t_func(a)
second_term = t_func(b)

sum_3 = float(0)

for kk in range(1, N, 2):
	sum_3 += t_func(a + (kk * h))

third_term = 4 * sum_3

sum_4 = float(0)

for kk in range(2, N, 2):
	sum_4 += t_func(a + (kk * h))

fourth_term = 2 * sum_4

simp_int = (h / 3) * (first_term + second_term + third_term + fourth_term)

print("Integral is {0}".format(simp_int))
