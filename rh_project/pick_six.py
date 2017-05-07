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
	period = np.sqrt(4 * np.pi**2 * a**3 / G / (M1 + M2)) # period in days

	print("Period is {0:.3f} days".format(period))

	v = 2 * np.pi * a / period  # AU/days

	return v

	
# def rk4_func(params):
# 	s1, s2, p, vs1, vs2, vp = params

# 	s1x, s1y = s1
# 	s2x, s2y = s2
# 	px, py = p

# 	# s1_vx, s1_vy = vs1
# 	# s2_vx, s2_vy = vs2
# 	# p_vx, p_vy = vp

# 	a1x = -G * red_mass * 0.1 / np.sqrt(0.1)**3
# 	a1y = -G * red_mass * 0 / np.sqrt(0.1)**3


# 	# R1px = abs(s1x - px)
# 	# R1py = abs(s1y - py)

# 	# R2px = abs(s2x - px)
# 	# R2py = abs(s2y - py)

# 	# R12x = abs(s1x - s2x)
# 	# R12y = abs(s1y - s2y)

# 	# R1p = np.sqrt((s1x - px)**2 + (s1y - py)*2)
# 	# R2p = np.sqrt((s2x - px)**2 + (s2y - py)*2)

# 	# R12 = A  # global variable

# 	# a1_2x = -G * M1 * R12x / R12**3
# 	# a1_2y = -G * M1 * R12y / R12**3

# 	# a2_1x = -G * M2 * R12x 

def ghetto(arr):

	x, y, vx, vy = arr


	ax = -G * red_mass * x / np.sqrt(x**2 + y**2)**3
	ay = -G * red_mass * y / np.sqrt(x**2 + y**2)**3

	ac_arr = np.array([ax, ay], float)

	# print(x)

	return np.array([vx, vy, ax, ay])


# Constants

G = 4 * np.pi**2  # AU^3 yr^-2 M_sun^-1

A = 0.2  # AU
r = A/2  # semi-major axis & radius
test_plan = 1 # AU

a = 0
b = .05
N = 100000
h = (b-a)/N

M1 = 1
M2 = 1

red_mass = M1*M2/(M1+M2)

tpoints = np.arange(a, b, h, dtype=int)


s1 = np.array([r, 0], float)
s2 = np.array([-r,0], float)
p = np.array([test_plan, 0], float)

# s_vel = find_vel_init(M1, red_mass, r)

s_vel = np.sqrt(10*G*red_mass)

p_vel = find_vel_init(red_mass, 0, test_plan)

print(s_vel)

s1_v0 = np.array([0, s_vel], float)
s2_v0 = np.array([0, -s_vel], float)
p_v0 = np.array([0, p_vel], float)

all_params = np.array([s1, s2, p, s1_v0, s2_v0, p_v0])

xpts_s1 = [[] for tt in range(len(tpoints))]
ypts_s1 = [[] for tt in range(len(tpoints))]

xpts_s2 = [[] for tt in range(len(tpoints))]
ypts_s2 = [[] for tt in range(len(tpoints))]

xpts_p = [[] for tt in range(len(tpoints))]
ypts_p = [[] for tt in range(len(tpoints))]

s_ghet = np.array([s1[0], s1[1], s1_v0[0], s1_v0[1]])

for tt in range(len(tpoints)):
	xpts_s1[tt] = s_ghet[0]
	ypts_s1[tt] = s_ghet[1]

	k1 = h * ghetto(s_ghet)
	k2 = h * ghetto(s_ghet + 0.5*k1)
	k3 = h * ghetto(s_ghet + 0.5*k2)
	k4 = h * ghetto(s_ghet + k3)

	s_ghet += (k1 + 2*k2 + 2*k3 + k4) / 6

	# print(s_ghet[0])

plt.plot(xpts_s1, ypts_s1)
plt.show()

# def f(s,t):
# 	x, y, vx, vy = s
# 	R = np.sqrt(x**2 + y**2)
# 	ax = (-GMsun * x )/R ** 3 
# 	ay = (-GMsun * y )/R ** 3 
# 	return np.array([vx, vy, ax, ay]) 


# r0 = np.array([r, 0.0], float)
# v0 = np.array([0, -s_vel], float)
# s = np.array([r0[0], r0[1], v0[0], v0[1]])	


# for tt in :
# 	solution[j] = s
# 	k1 = h*f(s,t)
# 	k2 = h*f(s+0.5*k1,t+0.5*h)
# 	k3 = h*f(s+0.5*k2,t+0.5*h)
# 	k4 = h*f(s+k3,t+h)
# 	s += (k1+2*k2+2*k3+k4)/6