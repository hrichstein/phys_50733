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
from scipy.constants import k

from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# print(k)

# T = float(input("Please enter the temperature in Kelvin: "))

rho = 6.022e28  # m^-3
debye_t = 428  # K
V = 1000  # cm^3 of solid aluminum


def inner_func(x):
	numerator = (x**4) * exp(x)
	denominator = (exp(x) - 1)**2

	if denominator == 0:
		print("x={0}".format(x))

	return numerator / denominator


def cv(T):
	a = 0
	b = debye_t / T
	N = 1000
	h = (b - a) / N

	first_term = 0.  # if put into the function, would return NaN
	second_term = (1 / 2) * inner_func(b)

	summ = float(0)

	for nn in arange(1, N, 1):
		summ += inner_func((a + (nn * h)))

	integral = h * (first_term + second_term + summ)

	c_v = 9 * V * rho * k * ((T / debye_t)**3) * integral

	return c_v

# h_cap = cv(T)

temp_arr = arange(5, 505, 5)

hc_arr = [[] for tt in range(len(temp_arr))]

for tt in range(len(temp_arr)):
	hc_arr[tt] = cv(temp_arr[tt])

hc_arr = array(hc_arr) / 1000

fig, ax = plt.subplots()
ax.plot(temp_arr, hc_arr, color="purple")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Heat Capacity (kJ)")
ax.set_title("Heat Capacity vs. Temperature")
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2e'))

plt.tight_layout()
plt.show()

# print("The heat capacity is {0}".format(h_cap))
