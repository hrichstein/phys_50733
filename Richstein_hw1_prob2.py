"""
-------------------------------------------------------------------------------
Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 1, Problem 2
Last edited: 29 Jan 2017

Overview:
---------
This program asks the user for an orbital period in minutes and calculates the 
altitude a satellite must have in meters to remain in orbit around the Earth.

Input:
------
Period, in minutes.

Output:
-------
Altitude, in meters. Scientific notation with three significant figures. 

Program Limitations:
--------------------
N/A

Significant Program Variables:
------------------------------
T: float-like
    The period of the orbiting satellite in minutes

h: float-like
    The required altitude in meters of a satellite orbiting Earth with period T

"""

from __future__ import division, absolute_import
from numpy import pi

#Setting constants
G = 6.67e-11     #m**3 kg**-1 s**-2, Newton's gravitational constant
M = 5.97e24      #kg, Mass of the Earth
R = 6371 * 10**3 #m, Radius of the Earth

#Asking for user input
T = input("Please enter the desired period, T, in minutes: ")
T *= 60

#Calculating the desired value
h = ( (G*M*(T**2)) / (4*(pi**2)) )**(1/3) - R 

#Printing the value to the screen
print("The required altitude h, in meters is {0:1.2e}".format(h))

#END PROGRAM

"""
2a)

For a planet or satellite orbiting a central body of mass M,

(T / (2*pi) )**2 = a**3 / (G * M)

where T is period in seconds, a is the radius of a circular orbit, and G is
Newton's gravitational constant.

(From this equation, we see Kepler's third law of planetary motion, that the 
square of the orbital period is proportional to the cube of the semi-major
axis.)

We split a, the full radius, to be h + R, where R is the radius of the Earth 
and h is the altitude the satellite must be above the Earth's surface.

(T / (2*pi) )**2 = (R + h)**3 / (G*M)

We then solve for h.

T**2 / (4*(pi**2)) * (G*M) = (R + h)**3

G*M*(T**2) / (4*(pi**2)) = (R + h)**3

( (G*M*(T**2)) / (4*(pi**2)) )**(1/3) = R + h

( (G*M*(T**2)) / (4*(pi**2)) )**(1/3) - R = h

h = ( (G*M*(T**2)) / (4*(pi**2)) )**(1/3) - R

which matches equation (1) on the assignment sheet.

2c)

T = 24*60 min (1 day),  h =  3.59e+07
T = 90 min,             h =  2.79e+05
T = 45 min,             h = -2.18+06

From the last of these calculations, we can conclude that there cannot be a
satellite which orbits the Earth every 45 minutes.

2d)

The sidereal day is how long it takes for the Earth to make a full rotation on 
its axis relative to very distant, or "fixed," stars.  It takes into account
Earth's rotation as well as its progress in its orbit around the Sun.

T = 23.93 * 60 min (1 sidereal day), h = 3.58e+07

This made a difference in required altitude of about 0.01e+07, or 1.00e+05 m.
A geosynchronous satellite requires an altitude of about 100,000 meters less
than one which has a period of 24 hours, a solar day.
"""