import numpy as np
import matplotlib.pyplot as plt
# from scipy.constants import G

# Setting plotting parameters
from matplotlib import rc,rcParams
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rc('font', **{'family': 'serif', 'serif':['Computer Modern']})

def find_vel_init(M1, M2, a):
	period = np.sqrt(4 * np.pi**2 * a**3 * 365.25**2 / G / (M1 + M2)) # period in days

	print("Period is {0:.3f} days".format(period))

	v = 2 * np.pi * a / period  # AU/days

	return v


def star_accel(theta_arr, r):
	"""
	theta_arr is an array with the angles for s1 and s2 (from the x-axis to the center of mass)
	"""

	# How far apart these are to begin with
	# rsep = r**2 + r**2 - 2*r*r*np.cos((theta_arr[1]-theta_arr[0])*np.pi/180)
	rsep = r*2

	# How much the angle changes
	d_theta = G*(M1+M2)*r / rsep**2
	
	return d_theta

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
											  (p[1] - s1[1])**2)**2\
		 +(-G * M2 * (p[0]-s2[0]) )/ (np.sqrt((p[0] - s2[0])**2) +\
											  (p[1] - s2[1])**2)**2

	a_y = (-G * M1 * (p[1]-s1[1]) )/ (np.sqrt((p[0] - s1[0])**2) +\
											  (p[1] - s1[1])**2)**2\
		 +(-G * M2 * (p[1]-s2[1]) )/ (np.sqrt((p[0] - s2[0])**2) +\
											  (p[1] - s2[1])**2)**2

	return np.array([a_x, a_y])	

def rk4_func(param_arr):

	s1 = param_arr[0]
	s2 = param_arr[1]
	p = param_arr[2]
	d_p_pos = param_arr[3]

	accels = plan_accel(s1, s2, p)

	dx_s = r * np.cos(d_theta * np.pi/180)
	dy_s = r * np.sin(d_theta * np.pi/180)

	d_s_pos = np.array([dx_s, dy_s])

	d_p_v = h * accels

	# d_theta_arr = np.array([d_theta, d_theta])

	return np.array([d_s_pos, d_s_pos, d_p_pos, d_p_v])


G = 4 * np.pi**2 # AU^3 yr^-2 M_sun^-1


a = 0
b = .05 # years
N = 100000
h = (b-a)/N

M1 = 1    
M2 = 1

red_mass = M1 * M2 / (M1 + M2)

tpoints = np.arange(a, b, h)

# Initial Conditions

A = 0.2  # AU
r = A/2  # semi-major axis & radius
planet_test_r = 4 # AU

theta_1 = 0
theta_2 = 180

theta_arr = np.array([theta_1, theta_2])
d_theta = star_accel(theta_arr, r)

# s1_init = np.array([r, 0])
# s2_init = np.array([-r, 0])
p_init = np.array([planet_test_r, 0])

# s_yvel = find_vel_init(M1, M2, r)
p_yvel = find_vel_init(0, red_mass, planet_test_r)

# s1_v_init = np.array([0, s_yvel])
# s2_v_init = np.array([0, -s_yvel])
p_v_init = np.array([0, p_yvel])

# all_params = np.array([theta_arr, p_init])

# Empty arrays

xpts_s1 = [[] for tt in range(len(tpoints))]
ypts_s1 = [[] for tt in range(len(tpoints))]

xpts_s2 = [[] for tt in range(len(tpoints))]
ypts_s2 = [[] for tt in range(len(tpoints))]

xpts_p = [[] for tt in range(len(tpoints))]
ypts_p = [[] for tt in range(len(tpoints))]

s1_pos = np.array([r, 0])
s2_pos = np.array([-r, 0])


rk_params = np.array([s1_pos, s2_pos, p_init, p_v_init])


for tt in range(len(tpoints)):
	# xpts_s1[tt] = r * np.cos(all_params[0][0] * np.pi/180)
	# ypts_s1[tt] = r * np.sin(all_params[0][0] * np.pi/180)

	xpts_s1[tt] = rk_params[0][0]
	ypts_s1[tt] = rk_params[0][1]

	# s1_pos = np.array([xpts_s1[tt], ypts_s1[tt]])

	# xpts_s2[tt] = r * np.cos(all_params[0][1] * np.pi/180)
	# ypts_s2[tt] = r * np.sin(all_params[0][1] * np.pi/180)

	# s2_pos = np.array([xpts_s2[tt], ypts_s2[tt]])

	xpts_s2[tt] = rk_params[1][0]
	xpts_s2[tt] = rk_params[1][1]

	xpts_p[tt] = rk_params[2][0]
	ypts_p[tt] = rk_params[2][1]

	# p_pos = np.array([xpts_p[tt], ypts_p[tt]])


	k1 = h * rk4_func(rk_params)
	k2 = h * rk4_func(rk_params + 0.5*k1)
	k3 = h * rk4_func(rk_params + 0.5*k2)
	k4 = h * rk4_func(rk_params + k3)
	rk_params += (k1 + 2*k2 + 2*k3 + k4) / 6

	# all_params[0] = rk_params[4]
	# all_params[1] = rk_params[2]

plt.plot(xpts_s1,ypts_s1, label="Star 1")
plt.plot(xpts_s2,ypts_s2, label="Star 2")
plt.plot(xpts_p,ypts_p, label="Planet")
plt.legend()
plt.show()	