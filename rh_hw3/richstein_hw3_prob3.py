"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 3: Heat capacity of a solid
Last edited: 15 February 2017

Overview:
---------
This program uses Debye's theory of solids to calculate the heat capacity of a
solid at temperature T, with volume V, density rho, and Debye temperature
debye_t. It uses the trapezoidal rule to calculate the integral

Input:
------
None

Output:
-------
A plot showing heat capacity as a function of temperature

"""

from numpy import exp, arange, array
from scipy.constants import k
from matplotlib import pyplot as plt


rho = 6.022e28  # m^-3
debye_t = 428  # K
V = 1e-3  # m^3 of solid aluminum
# Units on k are J/K (Joules per Kelvin)


def inner_func(x):  # the function being integrated
	numerator = (x**4) * exp(x)
	denominator = (exp(x) - 1)**2

	return numerator / denominator


def cv(T):
	a = 0
	b = debye_t / T
	N = 1000
	h = (b - a) / N

	first_term = 0.  # if you put "a" into the function, would return NaN
					 # Following hint that the integrand at x = 0 is 0
	second_term = (1 / 2) * inner_func(b)

	summ = float(0)

	for nn in arange(1, N, 1):
		summ += inner_func((a + (nn * h)))

	integral = h * (first_term + second_term + summ)

	c_v = 9 * V * rho * k * ((T / debye_t)**3) * integral

	return c_v


temp_arr = arange(5, 505, 5)  # Chose step-size of 5, because anything larger
							  # that evenly divided the section (ex: 15, 45)
							  # created plots not as smooth

# An array to hold the heat capacity values
hc_arr = [[] for tt in range(len(temp_arr))]

for tt in range(len(temp_arr)):
	hc_arr[tt] = cv(temp_arr[tt])

# Convertaing to kJ, just because the numbers are so large
hc_arr = array(hc_arr)

fig, ax = plt.subplots()
ax.plot(temp_arr, hc_arr, color="purple")
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Heat Capacity (J/K)")
ax.set_title("Heat Capacity vs. Temperature")

plt.tight_layout()
plt.show()

# END PROGRAM
