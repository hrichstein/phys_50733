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
	period = np.sqrt(4 * np.pi**2 * a**3 / G / (M1 + M2)) # period in years

	print("Period is {0:.3f} years".format(period))

	v = 2 * np.pi * a / period  # AU/year

	print(v)

	return v

def ghetto2(param):

	s1, s2, vs1, vs2 = param
	s1x, s1y = s1
	s2x, s2y = s2

	RS = np.sqrt((s1x-s2x)**2 + (s1y-s2y)**2)

	a1x = -G * red_mass * s1x / np.sqrt(s1x**2 + s1y**2)**3
	# a1x += (-G * M2 * (s1x - s2x) / RS**3)

	a1y = -G * red_mass * s1y / np.sqrt(s1x**2 + s1y**2)**3
	# a1y += (-G * M2 * (s1y - s2y) / RS**3)

	a2x = -G * red_mass * s2x / np.sqrt(s2x**2 + s2y**2)**3
	# a2x += (-G * M1 * (s2x - s1x) / RS**3)

	a2y = -G * red_mass * s2y / np.sqrt(s2x**2 + s2y**2)**3
	# a2y += (-G * M1 * (s2y - s1y) / RS**3)

	a1 = np.array([a1x, a1y])
	a2 = np.array([a2x, a2y])

	return np.array([vs1, vs2, a1, a2])

G = 4 * np.pi**2  # AU^3 yr^-2 M_sun^-1

A = 0.2  # AU
r = A/2  # semi-major axis & radius
test_plan = 1 # AU

a = 0
b = .02
N = 100000
h = (b-a)/N

M1 = 1
M2 = 1

red_mass = M1*M2/(M1+M2)

tpoints = np.arange(a, b, h, dtype=int)	

s1 = np.array([r, 0], float)
s2 = np.array([-r,0], float)

# s_vel = find_vel_init(M1, red_mass, r)

# s_vel = 20

s_vel = np.sqrt(10*G*red_mass)

print("S-vel : {0:.2f}".format(s_vel))

s1_v0 = np.array([0, s_vel], float)
s2_v0 = np.array([0, -s_vel], float)


xpts_s1 = [[] for tt in range(len(tpoints))]
ypts_s1 = [[] for tt in range(len(tpoints))]

xpts_s2 = [[] for tt in range(len(tpoints))]
ypts_s2 = [[] for tt in range(len(tpoints))]

s_ghet = np.array([s1, s2, s1_v0, s2_v0])

for tt in range(len(tpoints)):
	xpts_s1[tt] = s_ghet[0][0]
	ypts_s1[tt] = s_ghet[0][1]

	xpts_s2[tt] = s_ghet[1][0]
	ypts_s2[tt] = s_ghet[1][1]

	k1 = h * ghetto2(s_ghet)
	k2 = h * ghetto2(s_ghet + 0.5*k1)
	k3 = h * ghetto2(s_ghet + 0.5*k2)
	k4 = h * ghetto2(s_ghet + k3)

	s_ghet += (k1 + 2*k2 + 2*k3 + k4) / 6

plt.plot(xpts_s1, ypts_s1)
plt.plot(xpts_s2, ypts_s2)
plt.show()	