"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 6: Nonlinear Pendulum
Last edited: 7 April 2017

Overview:
---------


Input:
------


Output:
-------


"""
import numpy as np
from matplotlib import pyplot as plt


# take user input to say which solver to use and where to start

# a)

# Fourth order Runga Kutta

# General 

theta_init = 177 # degrees from vertical
arm_length = 0.05 # meters

g = 9.81
h = 0.5 # step size

# d_theta = omega 8.45
# d_omega = -g/l sin(theta) 8.46

# define some function here

def pend_func(r,t):
	theta = r[0]
	omega = r[1]
	d_theta = omega
	d_omega = -(g/l)*np.sin(theta*np.pi/180)
	return np.array([d_theta,d_omega],float)

a = 0.0  # first time step
b = 10.0  # last time step
N = 10  # Number of steps
h = (b-a)/N  # step size

tpoints = np.arange(a, b, h)
xpoints = []
x = 0.0

for t in tpoints:
	xpoints.append(x)
	k1 = h * pend_func(x,t)
	k2 = h * pend_func(x + 0.5*k1, t + 0.5*h)
	k3 = h * pend_func(x + 0.5*k2, t + 0.5*h)
	k4 = h * pend_func(x + k3, t + h)
	x += (k1+2*k2+2*k3+k4)/6

# b)

# Leapfrog

theta_2_init = -92 # degrees 
x2 = 0.0

f1 = x2 + 0.5*h*pend_func




# For making gifs

# images = []
# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.mimsave('/path/to/movie.gif', images)


# import imageio
# with imageio.get_writer('/path/to/movie.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)