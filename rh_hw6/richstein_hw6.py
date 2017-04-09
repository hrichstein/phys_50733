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

r = [theta_init, 0]

def pend_func(r,t):
	# print(r)
	theta = r[0]  # in degrees
	omega = r[1]
	d_theta = omega
	d_omega = -(g/arm_length)*np.sin(theta*np.pi/180)

	return np.array([d_theta,d_omega],float)


a = 0.0  # first time step
b = 10.0  # last time step
# N = 10  # Number of steps
# h = (b-a)/N  # step size

tpoints = np.arange(a, b, h)
xpoints = []  # actualy theta values
x = r

for t in tpoints:
	xpoints.append(x[0])  # theta values
	k1 = h * pend_func(x,t)
	k2 = h * pend_func(x + 0.5*k1, t + 0.5*h)
	k3 = h * pend_func(x + 0.5*k2, t + 0.5*h)
	k4 = h * pend_func(x + k3, t + h)
	x += (k1+2*k2+2*k3+k4)/6
	# print(x)

# b)

# Leapfrog

theta_2_init = -92 # degrees 
x2points = []

r2 = [theta_2_init, 0]
x2 = r2

def leapfrog(init, half, t, array):
	next_full = init + h * pend_func(half, t + 0.5*h)
	array.append(next_full[0])
	next_half = half + h * pend_func(next_full, t + h)
	array.append(next_half[0])

	return np.array([next_full,next_half])


x2points.append(x2[0])
f0 = r2[0]
f1 = x2 + 0.5*h * pend_func(x2, t)  # x(t+0.5h)

input_arr = [f0,f1]

for t in tpoints:
	input_arr = leapfrog(input_arr[0], input_arr[1], t, x2points)



# f1 = x2 + 0.5*h * pend_func(x2, t)  # x(t+0.5h)



# f2 = x2 + h * pend_func(f1, t + 0.5*h)  # x(t+h)
# f3 = f1 + h * pend_func(f2, t + h)  # x(t+1.5h)
# f4 = f2 + h * pend_func(f3, t + h)  # x(t+2h)




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