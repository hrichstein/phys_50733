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

from numpy import exp, arange, array

from matplotlib import pyplot as plt

a = 0
b = 3
N = 30
# h = (b - a) / N


def t_func(x):
	result = exp(x**2)

	return result

x_arr = arange(0, 3.1, 0.1)

# first_term = t_func(a)
# second_term = t_func(b)

# sum_3 = float(0)
# sum_4 = float(0)

# for xx in x_arr:
# 	for kk in range(1, N, 2):
# 		sum_3 += t_func(a + (kk * h))

# 	third_term = 4 * sum_3

# 	for kk in range(2, N, 2):
# 		sum_4 += t_func(a + (kk * h))

# 	fourth_term = 2 * sum_4

# 	simp_int = (h / 3) * (first_term + second_term + third_term + fourth_term)

# # print("Integral is {0}".format(simp_int))

# first_range = arange(1, 10, 2)
# second_range = arange(2, 11, 2)

# int_val_arr = [[] for xx in range(len(x_arr))]

# for xx in range(len(x_arr)):
# 	sum_3 += t_func(a + (first_range[xx] * h))
# 	sum_4 += t_func(a + (second_range[xx] * h))

# 	simp_int = (h / 3) * (first_term + second_term + (4 * sum_3) + (2 * sum_4))

# 	int_val_arr[xx] = simp_int

kk = 1


def int_steps(a, b, N):
	h = (b - a) / N

	sum_3 = float(0)
	sum_4 = float(0)

	first_term = t_func(a)
	second_term = t_func(b)

	for kk in range(1, N, 2):
		sum_3 += t_func(a + (kk * h))

	third_term = 4 * sum_3
	
	print("third term : {0}".format(third_term))
	for kk in range(2, N, 2):
		sum_4 += t_func(a + (kk * h))

	fourth_term = 2 * sum_4

	print("fourth term : {0}".format(fourth_term))

	simp_int = (h / 3) * (first_term + second_term + third_term + fourth_term)

	return simp_int

int_val_arr = [[] for xx in range(len(x_arr))]
int_val_arr[0] = 0

little_areas = [[] for xx in range(len(x_arr))]
little_areas[0] = 0

summ = 0

for xx in range(len(x_arr) - 1):
	a = x_arr[xx]
	b = x_arr[xx + 1]

	little_areas[xx + 1] = int_steps(a, b, 10)

	summ += little_areas[xx + 1]

	int_val_arr[xx + 1] = summ

	print("x is {0} and integral is {1}".format(x_arr[xx], int_val_arr[xx + 1]))

int_val_arr = array(int_val_arr)

plt.plot(x_arr, int_val_arr)
plt.show()	