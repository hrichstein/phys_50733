"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 2, Prob 2 - The semi-empirical mass formula
Last edited: 7 February 2017

Overview:
---------
This program calculates and returns the binding energy and binding energy per
nucleon of an atom.

Input:
------
The user must input A, the mass number, and Z, the atomic number.

Output:
-------
This will print the binding energy B, in MeV, and the binding energy per
nucleon in MeV.

Program Limitations:
--------------------
N/A

Significant Program Variables:
------------------------------
A: user-input mass number

Z: user-input atomic number

a_n: coefficients for the nth term in the sum

B: calculated binding energy

"""

# Importing because I like np arrays and didn't want to mess with regular ones.
from numpy import array

# Constants (Set Coefficients)
a_1 = 15.67
a_2 = 17.23
a_3 = 0.75
a_4 = 93.2

# Mass number is number of protons
A   = int(input("Please input the mass number of the atom: "))

# Atomic number is number of protons + number of neutrons
Z   = int(input("\nPlease input the atomic number of the atom: "))

# Calculating the binding energy for the atom and per nucleon


def binding_energy(A, Z):

	if A % 2   !=   0:
		a_5     =   0
	elif Z % 2 ==   0:
		a_5     =  12.0
	else:
		a_5     = -12.0

	# print("\na_5 = {0}".format(a_5))  #Checking to see if loop is working

	first_term = a_1 * A
	sec_term   = a_2 * ( (A)**(2/3) )
	third_term = a_3 * (Z**2) / ( A**(1/3) )
	four_term  = a_4 * ( ( A - (2*Z) )**2 ) / A
	fifth_term = a_5 / ( A**(1/2) )

	B = first_term - sec_term - third_term - four_term - fifth_term
	
	per_nuc = B / A

	return array([B, per_nuc])


results = binding_energy(A, Z)

# Returning the answer to the user
print("\nThe binding energy, B, is {0:0.1f}".format(results[0]) + " MeV.")
print("\nThe binding energy per nucleon is {0:0.2f}".format(results[1]) /
	+ " MeV.")

# END PROGRAM
