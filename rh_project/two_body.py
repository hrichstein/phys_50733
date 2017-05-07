# Restricted Three-Body Problem

import numpy as np
import matplotlib.pyplot as plt
# from scipy.constants import G

# Setting plotting parameters
from matplotlib import rc,rcParams
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rc('font', **{'family': 'serif', 'serif':['Computer Modern']})

G = 4 * np.pi**2  # AU^3 yr^-2 M_sun^-1



# m_1 = 1 # Solar mass
# m_2 = 1 # Solar mass

# mu = m_1 * m_2 / (m_1 + m_2) # Reduced mass
# M = m_1 + m_2

# r_maj = # Length of major axis; mean of the greatest and smallest distance apart of the two stars during their orbit

# r = np.array([r_maj * cos(theta),r_maj * sin(theta)])

# r_1 = -m_2 / (m_1 + m_2) * r # Position of first star (cm frame)
# r_2 = m_1 / (m_1 + m_2) * r # Position of second star

# r_cm = r_2 - r_1



# a_r = -G * M / r_cm**3 * r

# const = np.sqrt(r_maj * G * M)

# period = np.sqrt((4 * np.pi**2 * r_maj**3) / (G * M))


# r_3 # Position of third star

# a_1 = -G * m_2 * (r_1 - r_2) / (abs(r_1 - r_2))**3
# a_2 = -G * m_1 * (r_2 - r_1) / (abs(r_2 - r_1))**3
# a_3 = -G * m_1 * (r_3 - r_1) / (abs(r_3 - r_1))**3 - /
# 	   G * m_2 * (r_3 - r_2) / (abs(r_3 - r_2))**3


# a = # mean separation in AU
# period = np.sqrt(a**3 / (m_1 + m_2))  # years
# # masses in solar masses

# period = 2*pi/ angular acceleration

# period = 2* pi * r/v
# v = 2 * pi * r /T

# G is in Newton meter^2/kg^2
# Use f = Gmm/r^2 : r is distance between the centers 
# Find expressions for acceleration
# Find initial velocity using Kepler's third law (finding period)
# obtain initial velocities and positions, then plug into runga-kutta

# find period and acceleration then analytically find a circular orbit

# for runga-kutta, need x pos, y pos, x vel, y vel


# Newton's version of Kepler's 3rd Law
	# M1+M2 = A^3 / P^2
	# Masses in solar, semi-major axis in AU
	# 1 Msun is 1.99 * 10^30 kg
	# 1 AU is 149,600,000 km

def find_vel_init(M1, M2, A):
	period = np.sqrt(A**3 / (M1 + M2))

	v = 2 * np.pi * (A / 2) / period

	return v

A = 0.2  # AU

a = 0
b = 100
N = 250
h = (b-a) / N

tpoints = np.arange(a,b,h)

# initial velocity only in one direction
vx0 = find_vel_init(1, 1, A)

#Giving one a negative velocity

# x pos, y pos, x pos, y pos, xvel, yvel, xvel, yvel

all_params = np.array([0, 0.1, 0, -0.1, vx0, 0., -vx0, 0.])

def a_r(r1, r2):
	dx = 
	dy = 
	a = -G * m * (r1 - r2)/ abs(r1-r2)**3

	return a

def rk4(params, h):
	#First star positions
	x0_1 = params[0]
	y0_1 = params[1]
	#First star velocities
	vx0_1 = params[4]
	vy0_1 = params[5]


	#Second star positions
	x0_2 = params[2]
	y0_2 = params[3]
	#Second star velocities
	vx0_2 = params[6]
	vy0_2 = params[7]

	#First star accelerations
	ax1_1 = a_r(1,x0_1,x0_2)
	ay1_1 = a_r(1,y0_1,y0_2)

	#Second star accelerations
	ax1_2 = a_r(1,x0_1,x0_2)
	ay1_2 = a_r(1,y0_1,y0_2)

	################# STEP 1

	#First star
	x1_1 = x0_1 + 0.5*vx0_1*h
	y1_1 = y0_1 + 0.5*vy0_1*h
	#First star
	vx1_1 = vx0_1 + 0.5*ax1_1*h
	vy1_1 = vy0_1 + 0.5*ay1_1*h

	#Second star
	x1_2 = x0_2 + 0.5*vx0_2*h
	y1_2 = y0_2 + 0.5*vy0_2*h
	vx1_2 = vx0_2 + 0.5*ax1_2*h
	vy1_2 = vy0_2 + 0.5*ay1_2*h

	#First star accelerations
	ax2_1 = a_r(1,x1_1,x1_2)
	ay2_1 = a_r(1,y1_1,y1_2)

	#Second star accelerations
	ax2_2 = a_r(1,x1_1,x1_2)
	ay2_2 = a_r(1,y1_1,y1_2)

	################# STEP 2

	#First star
	x2_1 = x0_1 + 0.5*vx1_1*h
	y2_1 = y0_1 + 0.5*vy1_1*h
	vx2_1 = vx0_1 + 0.5*ax2_1*h
	vy2_1 = vy0_1 + 0.5*ay2_1*h

	#Second star
	x2_2 = x0_2 + 0.5*vx1_2*h
	y2_2 = y0_2 + 0.5*vy1_2*h
	vx2_2 = vx0_2 + 0.5*ax2_2*h
	vy2_2 = vy0_2 + 0.5*ay2_2*h

	#First star accelerations
	ax3_1 = a_r(1,x2_1,x2_2)
	ay3_1 = a_r(1,y2_1,y2_2)

	#Second star accelerations
	ax3_2 = a_r(1,x2_1,x2_2)
	ay3_2 = a_r(1,y2_1,y2_2)

	################# STEP 3

	#First star
	x3_1 = x0_1 + vx2_1*h
	y3_1 = y0_1 + vy2_1*h
	vx3_1 = vx0_1 + ax3_1*h
	vy3_1 = vy0_1 + ay3_1*h

	#Second star
	x3_2 = x0_2 + vx2_2*h
	y3_2 = y0_2 + vy2_2*h
	vx3_2 = vx0_2 + ax3_2*h
	vy3_2 = vy0_2 + ay3_2*h

	#First star accelerations
	ax4_1 = a_r(1,x3_1,x3_2)
	ay4_1 = a_r(1,y3_1,y3_2)

	#Second star accelerations
	ax4_2 = a_r(1,x3_1,x3_2)
	ay4_2 = a_r(1,y3_1,y3_2)

	#Final pos
	x1_f = x0_1 + h*(vx0_1 + 2*vx1_1 + 2*vx2_1 + vx3_1)/6
	x2_f = x0_2 + h*(vx0_2 + 2*vx1_2 + 2*vx2_2 + vx3_2)/6
	y1_f = y0_1 + h*(vy0_1 + 2*vy1_1 + 2*vy2_1 + vy3_1)/6
	y2_f = y0_2 + h*(vy0_2 + 2*vy1_2 + 2*vy2_2 + vy3_2)/6

	#Final vels
	vx1_f = vx0_1 + h*(ax1_1 + 2*ax2_1 + 2*ax3_1 + ax4_1)/6
	vx2_f = vx0_2 + h*(ax1_2 + 2*ax2_2 + 2*ax3_2 + ax4_2)/6
	
	vy1_f = vy0_1 + h*(ay1_1 + 2*ay2_1 + 2*ay3_1 + ay4_1)/6
	vy2_f = vy0_2 + h*(ay1_2 + 2*ay2_2 + 2*ay3_2 + ay4_2)/6

	# x pos, y pos, x pos, y pos, xvel, yvel, xvel, yvel
	
	new_params = np.array([x1_f,y1_f,x2_f,y2_f,vx1_f,vy1_f,vx2_f,vy2_f])

	return new_params

x1_points = [[] for tt in range(len(tpoints))]
y1_points = [[] for tt in range(len(tpoints))]

x2_points = [[] for tt in range(len(tpoints))]
y2_points = [[] for tt in range(len(tpoints))]


for tt in range(len(tpoints)):
	x1_points[tt] = all_params[0]
	y1_points[tt] = all_params[1]

	x2_points[tt] = all_params[2]
	y2_points[tt] = all_params[3]

	all_params = rk4(all_params, h)

plt.plot(x1_points,y1_points)
plt.plot(x2_points,y2_points)

plt.show()	


# a_1 = -G * m_2 * (r_1 - r_2) / (abs(r_1 - r_2))**3
# a_2 = -G * m_1 * (r_2 - r_1) / (abs(r_2 - r_1))**3

# put stars on opposite sides of zero
# given initial velocities and positions, then put into runga-kutta

# def grav_force(m1, m2, r_sep):
# 	"""
# 	m in solar masses
# 	r in AU
# 	"""
# 	force = G * m1 * m2 / r_sep**2

# 	return force

### Decompose acceleration equation into components
### For test cases, put planet super far out (assume massless) and then close to one star
