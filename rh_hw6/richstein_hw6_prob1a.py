"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 6: Nonlinear Pendulum - 4th-Order Runga-Kutta
Last edited: 24 April 2017

Overview:
---------
This script plots the motion of a nonlinear pendulum using the 4th-order 
Runga-Kutta method. It first shows theta as a function of time and then 
creates a series of .png files showing the motion of the pendulum.

Input:
------
None

Output:
-------
Plots to the screen a graph of theta vs time.
Saves series of images (every 25 timesteps) as .pngs in a directory

"""

# Importing Needed Modules
import numpy as np
from matplotlib import pyplot as plt
from scipy.constants import g

# Setting plotting parameters
from matplotlib import rc,rcParams
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rc('font', **{'family': 'serif', 'serif':['Computer Modern']})

# a)

# Fourth order Runga Kutta

# Defining Functions
def pend_func(r,t):
	"""
	This function takes in an array with a theta and omega value, as well as the timestep.

	Parameters
	----------

	r: array-like
		1D array with two values; the current theta and the angular frequency

	t: float-like
		The current time step (This doesn't seem to actually be used for anything, but helps to put in when visualizing how the Runga-Kutta works.)

	Output
	------
	An array containing values which will be added to the original array in later Runga-Kutta steps.

	"""

	theta = r[0]  # in degrees
	omega = r[1]
	d_theta = omega
	d_omega = -(g/arm_length)*np.sin(theta*np.pi/180)

	return np.array([d_theta,d_omega],float)


################
################
################

# Setting time constraints and creating timestep array
a = 0.0  # first time step
b = 10.0  # last time step
N = 1000  # Number of steps
h = (b-a)/N  # step size

tpoints = np.arange(a, b, h)

# Intial conditions for pendulum
theta_init = 177 # degrees from vertical
arm_length = 0.05 # meters

# Creating first array to be giving to pend_func
r = [theta_init, 0]

# Creating array to hold theta values
theta_points = [[] for tt in range(len(tpoints))]

# Implementing Runga-Kutta and filling an array with theta values
for tt in range(len(tpoints)):
	theta_points[tt] = r[0]
	k1 = h * pend_func(r,tt)
	k2 = h * pend_func(r + 0.5*k1, tt + 0.5*h)
	k3 = h * pend_func(r + 0.5*k2, tt + 0.5*h)
	k4 = h * pend_func(r + k3, tt + h)
	r += (k1+2*k2+2*k3+k4) / 6


# Plotting theta vs. time plot
fig, ax = plt.subplots()
ax.set_title(r"4th-Order Runga-Kutta, Theta Initial = $177^{\circ}$",size=18)
ax.set_xlabel("Time (seconds)",size=16)
ax.set_ylabel(r"Theta ($^{\circ}$)",size=16)
plt.plot(tpoints,theta_points)
plt.show()

###########
###########
###########

# Creating pendulum "animation" section

# Initializing two arrays to keep the Cartesian coordinates which will eventually be plotted
xpoints = [[] for xx in range(len(theta_points))]
ypoints = [[] for yy in range(len(theta_points))]

# Transforming the polar coordinates to Cartesian
for nn in range(len(theta_points)):
	trig_input = theta_points[nn]
	xpoints[nn] = arm_length * np.sin(trig_input * np.pi / 180)
	ypoints[nn] = arm_length * np.cos(trig_input * np.pi / 180)

# Creating and saving .pngs for every 25 timesteps
for rr in range(len(theta_points)):
	if rr%25 != 0:
		continue
	fig=plt.figure(figsize=(15,10))
	ax=fig.add_subplot(1,1,1)
	ax.set_xlim(-1.05*arm_length,1.05*arm_length)
	ax.set_ylim(-(1.05)*arm_length,1.05*arm_length)
	ax.set_xlabel(r"$Pendulum\ Beginning\ at\ 177^{\circ}$",size=20)
	ax.set_ylabel(r"$Y-Position\ (m)$",size=16)
	ax.set_title(r"$X-Position\ (m)$",y=1.05,size=16)
	ax.xaxis.set_ticks_position('top')
	plt.gca().invert_yaxis()
	x1, y1 = [0,xpoints[rr]], [0,ypoints[rr]]
	ax.text(0.02,-0.1*arm_length,"Theta: {0:.2f}, Time: {1}".format(theta_points[rr],tpoints[rr]))
	plt.plot(x1, y1, marker = 'o')
	plt.savefig("rk_plots/plot{}.png".format(rr))
	plt.close()