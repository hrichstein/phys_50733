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
from scipy.constants import c

x = float(input("Please input the distance to the desired planet in " 
	+ "light years: "))
v = float(input("\nPlease input the speed as a fraction of the speed of "
	+ "light.\n(For example, 0.75, to represent 0.75c.): "))

Julian_yr = 365.25


#1 ly = c * number of seconds in a year

x*= c * 3600 * 24 * Julian_yr  #Converting to meters
v*= c

gamma = 1 / ( ( 1 - ( (v**2)/(c**2)) )**(1/2) )

t_proper= x / v
t_rest  = t_proper * gamma

#Convert seconds to years
def sec_to_yr(seconds):
	return seconds / 3600 / 24/ Julian_yr


t_proper = sec_to_yr(t_proper)
t_rest   = sec_to_yr(t_rest)

print("\nThe time it takes to reach the planet as observed from Earth is "
	"{0:.2f}".format(t_rest) + " years.\n")
print("The time it takes as perceived by a passenger on the ship is "
	"{0:.2f}".format(t_proper) + " years.")