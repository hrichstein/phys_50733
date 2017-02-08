"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 2, Prob 1 - Special Relativity
Last edited: 7 February 2017

Overview:
---------
This program asks the user for the distance in light years to a planet and the
speed at which a spaceship is moving towards it as a fraction of the speed of
light. It then returns the time in years that it will take to reach the planet
as observed by someone on Earth and someone on the spaceship.

Input:
------
Distance in light years to a planet, speed as a fraction of the speed of light

Output:
-------
The time in years it will take the spaceship to reach the planet as seen by
someone on Earth, and the time in years it will take to do so as seen by
someone aboard the spaceship.

Program Limitations:
--------------------
N/A

Significant Program Variables:
------------------------------
c: speed of light in m/s

x: user-input, distance to planet in ly, then in m

v: user-input, fractional coefficient for the speed of light, later multiplied
   by the speed of light (c)

gamma: the factor which relates proper time and time in the inertial frame

t_proper: proper time (aboard spaceship)

t_rest: time as seen from Earth (rest frame)

"""
# Importing a constant for the speed of light
from scipy.constants import c

# Asking for user-input
x = float(input("Please input the distance to the desired planet in " /
	+ "light years: "))
v = float(input("\nPlease input the speed as a fraction of the speed of "
	+ "light.\n(For example, 0.75, to represent 0.75c.): "))

# Number of days in a Julian year (needed for converting to light years, etc.)
days_Julian_yr = 365.25

# Convert seconds to years
# 1 ly = c * number of seconds in a year


def sec_to_yr(seconds):
	return seconds / 3600 / 24 / days_Julian_yr


# Converting v and c to proper formats for calculation
x *= c * 3600 * 24 * days_Julian_yr  # Converting to meters
v *= c

# Calculating gamma
gamma = 1 / ( ( 1 - ( (v**2)/(c**2)) )**(1/2) )

# Time as seen aboard spaceship
t_proper = x / v

# Time as seen from Earth
t_rest   = t_proper * gamma

# Converting from seconds to years
t_proper = sec_to_yr(t_proper)
t_rest   = sec_to_yr(t_rest)

# Returning the answer to the user
print("\nThe time it takes to reach the planet as observed from Earth is " /
	  "{0:.2f}".format(t_rest) + " years.\n")
print("The time it takes as perceived by a passenger on the ship is " /
	  "{0:.2f}".format(t_proper) + " years.")

# END PROGRAM
