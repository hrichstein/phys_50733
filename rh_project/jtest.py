#########################################################################################
#	Computational Physics Project
#	
#	This program solves for the three-body motion of the Earth-Sun-Venus system using a 
#	fourth-order Runge-Kutta 
#
#	Units:
#	Distances : m
#	Gravitational constant (G) : m^3 kg^-1 s^-2 
#	Masses : kg 
#
#	Written by Jacqueline Antwi-Danso 04/17
#########################################################################################
import numpy as np 
import matplotlib.pyplot as plt
import pylab


def find_vel_init(M1, M2, a):
	period = np.sqrt(4 * np.pi**2 * a**3 * 365.25**2 / G / (M1 + M2)) # period in days

	print("Period is {0:.3f} days".format(period))

	v = 2 * np.pi * a / period  # AU/days

	return v



M1 = 1
M2 = 1

G = 4 * np.pi**2

red_mass = M1*M2/ (M1+M2)
#G = 6.67408E-11
#Msun = 1.989E30 
GMsun = 4*np.pi**2 * red_mass
#Me = 5.972E24
R0 = 0.1
#R0 = 1.496E11 

tau = 0.02

def f(s,t):
	x, y, vx, vy = s
	R = 0.1
	# R = np.sqrt(x**2 + y**2)
	ax = (-GMsun * x )/R ** 3 
	ay = (-GMsun * y )/R ** 3 
	return np.array([vx, vy, ax, ay]) 

vel0 = find_vel_init(M1, red_mass, R0)	

#tau = np.sqrt(((4*np.pi**2)/(G*(Msun+Me)))*R0**3)

a, b, N = 0.0,tau,1000000 #run simulation for one orbital period 
h = (b-a)/N 

time = np.arange(a,b,h)
r0 = np.array([R0, 0.0], float)
v0 = np.array([0, vel0], float)
s = np.array([r0[0], r0[1], v0[0], v0[1]])
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

plt.plot(x,y)
plt.show()

