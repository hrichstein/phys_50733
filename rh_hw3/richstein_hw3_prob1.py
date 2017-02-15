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

from pylab import imshow, show, gray, colorbar, xlabel, ylabel, title
from numpy import loadtxt

data = loadtxt("stm.txt", float)
imshow(data, origin='lower')
gray()
colorbar()
xlabel("X-Axis")
ylabel("Y-Axis")
title("Height of Silicon Surface")
show()
