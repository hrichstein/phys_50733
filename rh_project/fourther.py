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

def find_vel_init(M1, M2, a):
	"""
	Finds period and initial velocity using Newton's Form of Kepler's Third Law

	a is semi-major axis
	"""
	period = np.sqrt(4 * np.pi**2 * a**3 * 365.25**2 * 1440**2 / G / (M1 + M2)) # period in days

	print(period)

	v = 2 * np.pi * a / period  # AU/min

	return v

vs1 = find_vel_init(M1, M2, r)

# r1 = np.array([0.1,0])
# r2 = np.array([-0.1,0])

v1 = np.array([0,vs1])
v2 = np.array([0,-vs1])

# param_arr = np.array([r1,r2,v1,v2])

# def func(arr):
# 	r1 = arr[0]
# 	r2 = arr[1]

# 	v1 = arr[2]
# 	v2 = arr[3]

# 	R1 = np.sqrt(arr[0][0]**2 + arr[0][1]**2)
# 	ax1 = -G * (M1 + M2 * arr[0][0]) / R1**3
# 	ay1 = -G * (M1 + M2 * arr[0][1]) / R1**3

# 	acc1 = np.array([ax1, ay1])

# 	R2 = np.sqrt(arr[1][0]**2 + arr[1][1]**2)
# 	ax2 = -G * (M1 + M2) * arr[1][0] / R2**3
# 	ay2 = -G * (M1 + M2) * arr[1][1] / R2**3

# 	acc2 = np.array([ax2, ay2])

# 	return np.array([v1, v2, acc1, acc2])

# a = 0
# b = 0.005
# N = 1000000
# h = (b-a) / N

# tpoints = np.arange(a, b, h)

# xpts_s1 = [[] for tt in range(len(tpoints))]
# ypts_s1 = [[] for tt in range(len(tpoints))]

# xpts_s2 = [[] for tt in range(len(tpoints))]
# ypts_s2 = [[] for tt in range(len(tpoints))]

# for tt in range(len(tpoints)):
# 	xpts_s1[tt] = param_arr[0][0]
# 	ypts_s1[tt] = param_arr[0][1]

# 	xpts_s2[tt] = param_arr[1][0]
# 	ypts_s2[tt] = param_arr[1][1]

# 	k1 = h * func(param_arr)
# 	k2 = h * func(param_arr + 0.5*k1)
# 	k3 = h * func(param_arr + 0.5*k2)
# 	k4 = h * func(param_arr + k3)

# 	param_arr += (k1+2*k2+2*k3+k4)/6

# plt.plot(xpts_s1,ypts_s1, label="Star 1")
# plt.plot(xpts_s2,ypts_s2, label="Star 2")
# # plt.plot(xpts_p,ypts_p, label="Planet")
# plt.legend()
# plt.show()	

GM1 = 4*np.pi**2 * red_mass
#Me = 5.972E24
R0esun = 0.1
#R0esun = 1.496E11 

tau = 0.05

def f(s,t):
	x, y, vx, vy = s
	R = np.sqrt(x**2 + y**2)
	ax = (-GM1 * x )/R ** 3 
	ay = (-GM1 * y )/R ** 3 
	return np.array([vx, vy, ax, ay]) 

#tau = np.sqrt(((4*np.pi**2)/(G*(Msun+Me)))*R0esun**3)

a, b, N = 0.0,tau,100000 #run simulation for one orbital period 
h = (b-a)/N 

time = np.arange(a,b,h)
r0 = np.array([R0esun, 0.0], float)
# v0 = np.array([0, np.sqrt(np.sqrt(GM1/tau**2)-1)], float)
s = np.array([r0[0], r0[1], v1[0], v1[1]])
solution = np.empty(time.shape + s.shape,float)

for j,t in enumerate(time):
	solution[j] = s
	k1 = h*f(s,t)
	k2 = h*f(s+0.5*k1,t+0.5*h)
	k3 = h*f(s+0.5*k2,t+0.5*h)
	k4 = h*f(s+k3,t+h)
	s += (k1+2*k2+2*k3+k4)/6
	
x = solution[:,0]
y = solution[:,1]

############

GM2 = 4*np.pi**2 * red_mass

def g(s,t):
	x2, y2, vx2, vy2 = s
	R2 = np.sqrt(x2**2 + y2**2)
	ax2 = (-GM2 * x2 )/R2 ** 3 
	ay2 = (-GM2 * y2 )/R2 ** 3 
	return np.array([vx2, vy2, ax2, ay2]) 

#tau = np.sqrt(((4*np.pi**2)/(G*(Msun+Me)))*R0esun**3)


r02 = np.array([-R0esun, 0.0], float)
# v02 = np.array([0, - np.sqrt(np.sqrt(GM2/tau**2)-1)], float)
s2 = np.array([r02[0], r02[1], v2[0], v2[1]])
solution1 = np.empty(time.shape + s2.shape,float)

for j,t in enumerate(time):
	solution1[j] = s2
	k1 = h*f(s2,t)
	k2 = h*f(s2+0.5*k1,t+0.5*h)
	k3 = h*f(s2+0.5*k2,t+0.5*h)
	k4 = h*f(s2+k3,t+h)
	s2 += (k1+2*k2+2*k3+k4)/6
	
x2 = solution1[:,0]
y2 = solution1[:,1]

plt.plot(x2,y2)

plt.plot(x,y)
plt.show()