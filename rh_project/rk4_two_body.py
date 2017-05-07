import numpy as np
import matplotlib.pyplot as plt
# from scipy.constants import G

# Setting plotting parameters
from matplotlib import rc,rcParams
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rc('font', **{'family': 'serif', 'serif':['Computer Modern']})

def find_vel_init(M1, M2, A):
	period = np.sqrt(4 * np.pi**2 * A**3 / G / (M1 + M2)) # period in days

	v = 2 * np.pi * A / period  # AU/day

	return v

def accel(Mass, pos1, pos2):
	"""
	Mass: float-like?
		sum of the mass of both stars
	pos1: array-like
		[x,y] position of first star
	pos2: array-like
		[x,y] position of second star
	"""

	r_sep = np.sqrt((pos1[0] - pos1[1])**2 + (pos2[0] - pos2[1])**2)

	a_x = -G * Mass / r_sep**3 * abs(pos1[0] - pos2[0])
	a_y = -G * Mass / r_sep**3 * abs(pos1[1] - pos2[1])

	accel_arr = np.array([a_x, a_y])

	return accel_arr

# Gm(x1-x2)/r^3; r is the distance separating everything (both the stars)

# initial velocity only in one direction

def rk4(r1, r2, v1, v2, h):
	"""
	r: array-like
		has x,y components
	v: array-like
		has vx, vy components
	h: float-like
		time step
	"""
	x0_s1 = r1[0]
	y0_s1 = r1[1]

	x0_s2 = r2[0]
	y0_s2 = r2[1]

	d_x0_s1 = v1[0]
	d_y0_s1 = v1[1]

	d_x0_s2 = v2[0]
	d_y0_s2 = v2[1]

	d_v0 = accel(Mass, r1, r2)  # Same for both stars (velocity is what differs)

	# First set of RK4
	x1_s1 = x0_s1 + 0.5*(d_x0_s1)*h
	y1_s1 = y0_s1 + 0.5*(d_y0_s1)*h

	x1_s2 = x0_s2 + 0.5*(d_x0_s2)*h
	y1_s2 = y0_s2 + 0.5*(d_y0_s2)*h

	d_x1_s1 = d_x0_s1 + 0.5*(d_v0[0])*h
	d_y1_s1 = d_y0_s1 + 0.5*(d_v0[1])*h

	d_x1_s2 = d_x0_s2 + 0.5*(d_v0[0])*h
	d_y1_s2 = d_y0_s2 + 0.5*(d_v0[1])*h

	r1_new = np.array([x1_s1,y1_s1])
	r2_new = np.array([x1_s2,y1_s2])

	d_v1 = accel(Mass, r1_new, r2_new)

	# Second

	x2_s1 = x0_s1 + 0.5*(d_x1_s1)*h
	y2_s1 = y0_s1 + 0.5*(d_y1_s1)*h

	x2_s2 = x0_s2 + 0.5*(d_x1_s2)*h
	y2_s2 = y0_s2 + 0.5*(d_y1_s2)*h

	d_x2_s1 = d_x0_s1 + 0.5*(d_v1[0])*h
	d_y2_s1 = d_y0_s1 + 0.5*(d_v1[1])*h

	d_x2_s2 = d_x0_s2 + 0.5*(d_v1[0])*h
	d_y2_s2 = d_y0_s2 + 0.5*(d_v1[1])*h

	r1_new = np.array([x2_s1,y2_s1])
	r2_new = np.array([x2_s2,y2_s2])

	d_v2 = accel(Mass, r1_new, r2_new)

	# Third

	x3_s1 = x0_s1 + (d_x2_s1)*h
	y3_s1 = y0_s1 + (d_y2_s1)*h

	x3_s2 = x0_s2 + (d_x2_s2)*h
	y3_s2 = y0_s2 + (d_y2_s2)*h

	d_x3_s1 = d_x0_s1 + (d_v2[0])*h
	d_y3_s1 = d_y0_s1 + (d_v2[1])*h

	d_x3_s2 = d_x0_s2 + (d_v2[0])*h
	d_y3_s2 = d_y0_s2 + (d_v2[1])*h

	r1_new = np.array([x3_s1,y3_s1])
	r2_new = np.array([x3_s2,y3_s2])

	d_v3 = accel(1, r1_new, r2_new)

	# Combining

	xf_s1 = x0_s1 + h*(d_x0_s1 + 2*d_x1_s1 + 2*d_x2_s1 + d_x3_s1)/6
	yf_s1 = y0_s1 + h*(d_y0_s1 + 2*d_y1_s1 + 2*d_y2_s1 + d_y3_s1)/6

	rf_s1 = np.array([xf_s1,yf_s1])

	xf_s2 = x0_s2 + h*(d_x0_s2 + 2*d_x1_s2 + 2*d_x2_s2 + d_x3_s2)/6
	yf_s2 = y0_s2 + h*(d_y0_s2 + 2*d_y1_s2 + 2*d_y2_s2 + d_y3_s2)/6

	rf_s2 = np.array([xf_s2,yf_s2])

	d_xf_s1 = d_x0_s1 + h*(d_v0[0] + 2*d_v1[0] + 2*d_v2[0] + d_v3[0])/6
	d_yf_s1 = d_y0_s1 + h*(d_v0[1] + 2*d_v1[1] + 2*d_v2[1] + d_v3[1])/6

	vf_s1 = np.array([d_xf_s1,d_yf_s1])

	d_xf_s2 = d_x0_s2 + h*(d_v0[0] + 2*d_v1[0] + 2*d_v2[0] + d_v3[0])/6
	d_yf_s2 = d_y0_s2 + h*(d_v0[1] + 2*d_v1[1] + 2*d_v2[1] + d_v3[1])/6

	vf_s2 = np.array([d_xf_s2,d_yf_s2])

	results_arr = np.array([rf_s1, rf_s2, vf_s1, vf_s2])

	return results_arr

G = 4 * np.pi**2  # AU^3 yr^-2 M_sun^-1

Mass = 2  # Solar masses
A = 0.2  # AU (sep dist)

a = 0
b = 0.06  # years
N = 100000
h = (b-a) / N

tpoints = np.arange(a,b,h)	

# Setting up arrays

xpts_s1 = [[] for xx in range(len(tpoints))]
ypts_s1 = [[] for xx in range(len(tpoints))]

xpts_s2 = [[] for xx in range(len(tpoints))]
ypts_s2 = [[] for xx in range(len(tpoints))]

# Initial conditions
r0_s1 = np.array([0,0.1])
r0_s2 = np.array([0,-0.1])

vx0 = find_vel_init(1, 1, A)
vy0 = 0

v0_s1 = np.array([vx0,0])
v0_s2 = np.array([-vx0,0])

param_arr = np.array([r0_s1, r0_s2, v0_s1, v0_s2])

for tt in range(len(tpoints)):
	xpts_s1[tt] = param_arr[0][0]
	ypts_s1[tt] = param_arr[0][1]

	xpts_s2[tt] = param_arr[1][0]
	ypts_s2[tt] = param_arr[1][1]

	param_arr = rk4(param_arr[0], param_arr[1], param_arr[2], param_arr[3], h)

plt.plot(xpts_s1, ypts_s1)
plt.plot(xpts_s2, ypts_s2)

plt.show()
