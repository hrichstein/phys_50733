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
	period = np.sqrt(4 * np.pi**2 * A**3 * 365.25**2 / G / (M1 + M2)) # period in days

	print(period)

	v = 2 * np.pi * A / period  # AU/days

	return v

def orb_func(theta_arr):

	# How far apart these are to begin with
	# rsep = r**2 + r**2 - 2*r*r*np.cos((theta_arr[1]-theta_arr[0])*np.pi/180)
	
	# print(rsep)

	rsep = 0.2

	# How much the angle changes
	d_theta = G*(M1+M2)*r / rsep**2

	d_theta = np.sqrt(G*M1*M2*rsep) / rsep**2 / np.sqrt(M1*M2/(M1+M2))

	# print("Linear velocity is {0}".format(r*d_theta))

	new_th_arr = d_theta + theta_arr
	
	return new_th_arr


A = 0.2  # AU
r = A/2  # semi-major axis & radius
# G = 4 * np.pi**2
G = 4 * np.pi**2
a = 0
b = .05
N = 100000
h = (b-a)/N

M1 = 1
M2 = 1

print(find_vel_init(M1,M2,r))
print("AU / min")

tpoints = np.arange(a, b, h)

theta_1 = 0
theta_2 = 180 

th_arr = np.array([theta_1, theta_2],dtype=float)

theta_points1 = [[] for tt in range(len(tpoints))]
theta_points2 = [[] for tt in range(len(tpoints))]

for tt in range(len(tpoints)):
	theta_points1[tt] = th_arr[0]
	theta_points2[tt] = th_arr[1]
	k1 = h * orb_func(th_arr)
	k2 = h * orb_func(th_arr + 0.5*k1)
	k3 = h * orb_func(th_arr + 0.5*k2)
	k4 = h * orb_func(th_arr + k3)
	th_arr += (k1 + 2*k2 + 2*k3 + k4) / 6

xpoints1 = [[] for tt in range(len(tpoints))]
ypoints1 = [[] for tt in range(len(tpoints))]

xpoints2 = [[] for tt in range(len(tpoints))]
ypoints2 = [[] for tt in range(len(tpoints))]

for tt in range(len(tpoints)):
	xpoints1[tt] = r * np.cos(theta_points1[tt] * np.pi/180)
	ypoints1[tt] = r * np.sin(theta_points1[tt] * np.pi/180)

	xpoints2[tt] = r * np.cos(theta_points2[tt] * np.pi/180)
	ypoints2[tt] = r * np.sin(theta_points2[tt] * np.pi/180)

# r1 = np.array([(r*np.cos(theta_1*np.pi/180)), (r*np.sin(theta_1*np.pi/180))])
# r2 = np.array([(r*np.cos(theta_2*np.pi/180)), (r*np.sin(theta_2*np.pi/180))])

# def plan_accel(s1, s2, p1):
# 	"""
# 	s1: array-like
# 		x and y position of star 1
# 	s2: array-like
# 		x and y position of star 2
# 	p1: array-like
# 		x and y position of planet
# 	M1: integer-like (global variable)
# 		solar mass of each star (they're equal)
# 	"""

# 	a_x = (-G * M1 * (p1[0]-s1[0]) / (np.sqrt((p1[0] - s1[0])**2) +\
# 											  (p1[1] - s1[1])**2)**3)\
# 		 +(-G * M2 * (p1[0]-s2[0]) / (np.sqrt((p1[0] - s2[0])**2) +\
# 											  (p1[1] - s2[1])**2)**3)

# 	a_y = (-G * M1 * (p1[1]-s1[1]) / (np.sqrt((p1[0] - s1[0])**2) +\
# 											  (p1[1] - s1[1])**2)**3)\
# 		 +(-G * M2 * (p1[1]-s2[1]) / (np.sqrt((p1[0] - s2[0])**2) +\
# 											  (p1[1] - s2[1])**2)**3)

# 	accel_arr = np.array([a_x, a_y])

# 	return accel_arr

# def plan_fun(param_array, s1, s2):
# 	"""
# 	param_array: array-like
# 		param_array[0] = position of planet
# 		param_array[1] = velocity of planet
# 	s1: array-like
# 		x, y position of star 1
# 	s2: array-like
# 		x, y position of star 2

# 		Each of the above is array form with x and y components

# 	h: float-like
# 		global variable timestep
# 	"""
# 	x0 = param_array[0][0]
# 	y0 = param_array[0][1]

# 	vx0 = param_array[1][0]
# 	vy0 = param_array[1][1]

# 	dx = vx0 * h
# 	dy = vy0 * h

# 	d_pos = np.array([dx,dy])

# 	# print(s1)
# 	# print(s2)
# 	# print(param_array[0])

# 	accel_vals = plan_accel(s1,s2,param_array[0])

# 	dvx = accel_vals[0] * h
# 	dvy = accel_vals[1] * h

# 	d_vel = np.array([dvx,dvy])

# 	d_arr = np.array([d_pos, d_vel])

# 	return d_arr


# v_plan_init = find_vel_init(1,0,20)

# # Initial position

# pl_x0 = 2
# pl_y0 = 0

# pl_pos = np.array([pl_x0, pl_y0])

# # Initial Velocity

# pl_vx0 = 0
# pl_vy0 = v_plan_init

# pl_vel = np.array([pl_vx0, pl_vy0])

# plan_params = np.array([pl_pos, pl_vel])

# xpoints_p = [[] for tt in range(len(tpoints))]
# ypoints_p = [[] for tt in range(len(tpoints))]

# for tt in range(len(tpoints)):
# 	s1_pos = np.array([xpoints1[tt],ypoints1[tt]])
# 	s2_pos = np.array([xpoints2[tt],ypoints2[tt]])

# 	xpoints_p[tt] = plan_params[0][0]
# 	ypoints_p[tt] = plan_params[0][1]

# 	k1 = h * plan_fun(plan_params, s1_pos, s2_pos)
# 	k2 = h * plan_fun(plan_params + 0.5*k1, s1_pos, s2_pos)
# 	k3 = h * plan_fun(plan_params + 0.5*k2, s1_pos, s2_pos)
# 	k4 = h * plan_fun(plan_params + k3, s1_pos, s2_pos)
# 	plan_params += (k1 + 2*k2 + 2*k3 + k4) / 6


plt.plot(xpoints1,ypoints1, label="Star 1")
plt.plot(xpoints2,ypoints2, label="Star 2")
# plt.plot(xpoints_p,ypoints_p, label="Planet")
plt.legend()
plt.show()



	# # # Positions for three bodies initially

	# # s1_0x = s1[0]
	# # s1_0y = s1[1]

	# # s2_0x = s2[0]
	# # s2_0y = s2[1]

	# # p_x = p[0]
	# # p_y = p[1]

	# # Velocities for three bodies initially

	# s1_0v_x = v_s1[0]
	# s1_0v_y = v_s1[1]

	# s2_0v_x = v_s2[0]
	# s2_0v_y = v_s2[1]

	# p_v_x = v_p[0]
	# p_v_y = v_p[1]