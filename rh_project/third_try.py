import numpy as np
import matplotlib.pyplot as plt
# from scipy.constants import G

# Setting plotting parameters
from matplotlib import rc,rcParams
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rc('font', **{'family': 'serif', 'serif':['Computer Modern']})

##### Defining Functions

def find_vel_init(M1, M2, a):
	"""
	Finds period and initial velocity using Newton's Form of Kepler's Third Law

	a is semi-major axis
	"""
	period = np.sqrt(4 * np.pi**2 * a**3 * 365.25**2 * 1440**2 / G / (M1 + M2)) # period in days

	print(period)

	v = 2 * np.pi * a / period  # AU/min

	return v

def star_accel(s1, s2):
	r_sep = np.sqrt((s1[0]-s2[0])**2 + (s1[1]-s2[1])**2)

	a_x1 = (-G * M2 * (s1[0]-s2[0])) / r_sep**3
	a_x2 = (-G * M1 * (s2[0]-s1[0])) / r_sep**3

	a_y1 = (-G * M2 * (s1[1]-s2[1])) / r_sep**3
	a_y2 = (-G * M1 * (s2[1]-s1[1])) / r_sep**3

	a1 = np.array([a_x1, a_y1])
	a2 = np.array([a_x2, a_y2])

	return np.array([a1, a2])


def plan_accel(s1, s2, p):
	"""
	s1: array-like
		x and y position of star 1
	s2: array-like
		x and y position of star 2
	p: array-like
		x and y position of planet
	M1: integer-like (global variable)
		solar mass of each star (they're equal)
	"""

	a_x = (-G * M1 * (p[0]-s1[0]) )/ (np.sqrt((p[0] - s1[0])**2) +\
											  (p[1] - s1[1])**2)**3\
		 +(-G * M1 * (p[0]-s2[0]) )/ (np.sqrt((p[0] - s2[0])**2) +\
											  (p[1] - s2[1])**2)**3

	a_y = (-G * M1 * (p[1]-s1[1]) )/ (np.sqrt((p[0] - s1[0])**2) +\
											  (p[1] - s1[1])**2)**3\
		 +(-G * M1 * (p[1]-s2[1]) )/ (np.sqrt((p[0] - s2[0])**2) +\
											  (p[1] - s2[1])**2)**3

	return np.array([a_x, a_y])


def three_body_fun(params):
	"""
	s1: array-like
		x, y position for star 1
	s2: array-like
		x, y position for star 2
	p: array-like
		x, y position for planet
	v_s1: array-like
		vx, vy for star 1
	v_s2: array-like
		vx, vy for star 2
	v_p: array-like
		vx, vy for planet
	"""

	# Positions for three bodies initially
	s1 = params[0]
	s2 = params[1]
	p = params[2]
	v_s1 = params[3]
	v_s2 = params[4]
	v_p = params[5]

	s1_0x = s1[0]
	s1_0y = s1[1]

	s2_0x = s2[0]
	s2_0y = s2[1]

	p_x = p[0]
	p_y = p[1]



	# Finding accelerations

	s_accel = star_accel(s1, s2)
	s1_a = s_accel[0]
	s2_a = s_accel[1]

	p_accel = plan_accel(s1, s2, p)

	# Finding changes in positions

	d_s1_x = v_s1[0] * h
	d_s1_y = v_s1[1] * h

	new_s1 = np.array([d_s1_x, d_s1_y])

	d_s2_x = v_s2[0] * h
	d_s2_y = v_s2[1] * h

	new_s2 = np.array([d_s2_x, d_s2_y])

	d_p_x = v_p[0] * h
	d_p_y = v_p[1] * h

	new_p = np.array([d_p_x, d_p_y])

	# Finding changes in velocities

	d_s1_vx = s1_a[0] / np.sqrt(s1_0x**2 + s1_0y**2)
	d_s1_vy = s1_a[1] / np.sqrt(s1_0x**2 + s1_0y**2)

	new_v_s1 = np.array([d_s1_vx, d_s1_vy])

	d_s2_vx = s2_a[0] / np.sqrt(s2_0x**2 + s2_0y**2)
	d_s2_vy = s2_a[1] / np.sqrt(s2_0x**2 + s2_0y**2)

	new_v_s2 = np.array([d_s2_vx, d_s2_vy])

	d_p_vx = p_accel[0] / np.sqrt(p_x**2 + p_y**2)
	d_p_vy = p_accel[1] / np.sqrt(p_x**2 + p_y**2)

	new_v_p = np.array([d_p_vx, d_p_vy])

	return np.array([new_s1, new_s2, new_p, new_v_s1, new_v_s2, new_v_p])

# Constants

G = 4 * np.pi**2  # AU^3 yr^-2 M_sun^-1

A = 0.2  # AU
r = A/2  # semi-major axis & radius
test_plan = 5 # AU

a = 0
b = .01
N = 100000
h = (b-a)/N

M1 = 1
M2 = 1

red_mass = M1*M2/(M1+M2)

tpoints = np.arange(a, b, h)

# Setting up initial parameters

s1_0 = np.array([r, 0])
s2_0 = np.array([-r, 0])
p_0 = np.array([test_plan,0])

vs1 = find_vel_init(M1, M2, r)
vp = find_vel_init(red_mass,0, test_plan)

vs1_0 = np.array([0, vs1])
vs2_0 = np.array([0, -vs1])
vp_0 = np.array([0, vp])

all_params = np.array([s1_0, s2_0, p_0, vs1_0, vs2_0, vp_0])

# Setting up empty arrays

xpts_s1 = [[] for tt in range(len(tpoints))]
ypts_s1 = [[] for tt in range(len(tpoints))]

xpts_s2 = [[] for tt in range(len(tpoints))]
ypts_s2 = [[] for tt in range(len(tpoints))]

xpts_p = [[] for tt in range(len(tpoints))]
ypts_p = [[] for tt in range(len(tpoints))]

for tt in range(len(tpoints)):
	xpts_s1[tt] = all_params[0][0]
	ypts_s1[tt] = all_params[0][1]

	xpts_s2[tt] = all_params[1][0]
	ypts_s2[tt] = all_params[1][1]

	xpts_p[tt] = all_params[2][0]
	ypts_p[tt] = all_params[2][1]

	# Runga Kutta
	k1 = h * three_body_fun(all_params)
	k2 = h * three_body_fun(all_params + 0.5 * k1)
	k3 = h * three_body_fun(all_params + 0.5 * k2)
	k4 = h * three_body_fun(all_params + k3)

	all_params += (k1 + 2*k2 + 2*k3 + k4) / 6

plt.plot(xpts_s1,ypts_s1, label="Star 1")
plt.plot(xpts_s2,ypts_s2, label="Star 2")
plt.plot(xpts_p,ypts_p, label="Planet")
plt.legend()
plt.show()
