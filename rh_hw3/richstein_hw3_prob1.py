"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 3, Prob 1: Plotting experimental data
Last edited: 15 February 2017

Overview:
---------
This program reads in a grid of data and outputs a density plot

Input:
------
Data file: stm.txt

Output:
-------
A density plot showing the structure of a silicon surface

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
