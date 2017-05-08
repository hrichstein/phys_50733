"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
Project: Double Stars Planetary System
Last edited: 7 May 2017

Overview:
---------


Input:
------
None

Output:
-------


"""

# Importing needed modules
import numpy as np
import matplotlib.pyplot as plt

# Setting plotting parameters
from matplotlib import rc,rcParams
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rc('font', **{'family': 'serif', 'serif':['Computer Modern']})

# Defining functions
def find_vel_init(Mc, a):
	"""
	This function takes in the mass of the central body and the radius or 
	semi-major axis of the orbit.

	Parameters
	----------
	Mc: float-like
		Mass of the body which is being orbited; in solar masses

	a: float-like
		Distance from the orbiting object to the central object; in AU

	Output
	------
	v: float-like
		Velocity which orbiting body should initially be going if it were to
		go complete an orbit in the period solved for using Newton's version
		of Kepler's third law

	"""

	period = np.sqrt(4 * np.pi**2 * a**3 / G / (Mc)) # period in years

	print("\n Period is {0:.3f} years".format(period))

	v = np.sqrt(G * Mc * (2-1)/a)

	print("Initial velocity: {0:.2f} AU/years".format(v))

	# print(2*np.pi*a/v) Check for whether the circumference divided by the
	# velocity actually gave me the period found above

	return period, v

def rk4(param):

	"""
	This function takes in an array containing the positions and velocities of 
	the three bodies and determines the change in position and change in
	velocity for each. It then returns them in one array.

	Parameters
	----------
	param: numpy array-like
		An array with 6 other arrays within it:
			s1: x,y position of star 1
			s2: x,y position of star 2
			p: x,y position of planet
			vs1, vs2, vp: the x,y velocities of their respective bodies

	Output:
	------
	An array of the same format as what was input, except now with the
	derivatives of each quantity

	"""

	# Unpacking the gigantic array which is necessary for the Runge-Kutta to work
	s1, s2, p, vs1, vs2, vp = param
	s1x, s1y = s1
	s2x, s2y = s2
	px, py = p

	# Calculating the distances between the planet and each of the stars
	Rs1p = np.sqrt((s1x - px)**2 + (s1y - py)**2)
	Rs2p = np.sqrt((s2x - px)**2 + (s2y - py)**2)

	# Calculating the accelerations of the two stars; using the reduced mass,
	# equivalent one-body problem
	a1x = -G * red_mass * s1x / np.sqrt(s1x**2 + s1y**2)**3
	a1y = -G * red_mass * s1y / np.sqrt(s1x**2 + s1y**2)**3

	a2x = -G * red_mass * s2x / np.sqrt(s2x**2 + s2y**2)**3
	a2y = -G * red_mass * s2y / np.sqrt(s2x**2 + s2y**2)**3

	# Calculating the accelerations due to both stars on the planet
	apx = (-G * M1 * (px - s1x) / Rs1p**3) + (-G * M2 * (px - s2x) / Rs2p**3)
	apy = (-G * M1 * (py - s1y) / Rs1p**3) + (-G * M2 * (py - s2y) / Rs2p**3)

	# Packing these into arrays to return
	a1 = np.array([a1x, a1y])
	a2 = np.array([a2x, a2y])
	ap = np.array([apx, apy])

	return np.array([vs1, vs2, vp, a1, a2, ap])


# Defining constants
G = 4 * np.pi**2  # AU^3 yr^-2 M_sun^-1

# The separation between the binary stars
A = 20  # AU
r = A/2  # semi-major axis & radius of circle they will be orbiting

# Testing radius of planet
test_plan = 200  # AU

test_plan_arr = np.arange(230, 300, 10)

# Mass Settings
M1 = 1
M2 = 1

red_mass = M1*M2/(M1+M2)  # Reduced mass

for xx in test_plan_arr:

	test_plan = xx

	print("Case for Binary Stars separated by {0} AU and planet starting at "\
		"{1} AU from center of mass.".format(A, test_plan))

	# Calculating initial velocities
	print("\nFor Stars:")
	s_period, s_vel = find_vel_init(red_mass, r)
	print("\nFor Planet")
	p_period, p_vel = find_vel_init(red_mass, test_plan)

	E = (0.5*p_vel**2) - (G*red_mass/test_plan)
	print(r"Energy coefficient (to be multiplied by Earth mass): {0:.2f} AU$^2$/yr$^2$").format(E)

	# Time setup
	a = 0
	b = p_period
	N = 5e6
	h = (b-a)/N

	tpoints = np.arange(a, b, h, dtype=int)	

	# Initial conditions
		# Positions
	s1 = np.array([r, 0], float)
	s2 = np.array([-r,0], float)
	p = np.array([test_plan, 0], float)
		# Velocities
	s1_v0 = np.array([0, s_vel], float)
	s2_v0 = np.array([0, -s_vel], float)
	p_v0 = np.array([0, p_vel], float)

	# Creating empty arrays to be filled during the Runge-Kutta process
	xpts_s1 = [[] for tt in range(len(tpoints))]
	ypts_s1 = [[] for tt in range(len(tpoints))]

	xpts_s2 = [[] for tt in range(len(tpoints))]
	ypts_s2 = [[] for tt in range(len(tpoints))]

	xpts_p = [[] for tt in range(len(tpoints))]
	ypts_p = [[] for tt in range(len(tpoints))]

	# Array to be passed to Runge-Kutta
	rk_params = np.array([s1, s2, p, s1_v0, s2_v0, p_v0])

	# Flag-like variable to tell me if the Runge-Kutta stopped due to the planet
	# exceeding three times its escape velocity (Why keep running it after you
	# know it's being flung out)
	final_time = 0

	# Runge-Kutta implementation
	for tt in range(len(tpoints)):
		# Saving x and y points for plotting
		xpts_s1[tt] = rk_params[0][0]
		ypts_s1[tt] = rk_params[0][1]

		xpts_s2[tt] = rk_params[1][0]
		ypts_s2[tt] = rk_params[1][1]

		xpts_p[tt] = rk_params[2][0]
		ypts_p[tt] = rk_params[2][1]

		# Actual Runge-Kutta
		k1 = h * rk4(rk_params)
		k2 = h * rk4(rk_params + 0.5*k1)
		k3 = h * rk4(rk_params + 0.5*k2)
		k4 = h * rk4(rk_params + k3)

		rk_params += (k1 + 2*k2 + 2*k3 + k4) / 6

	# 	# Checking to see if the planet has been flung off yet
		vel = np.sqrt(rk_params[-1][0]**2 + rk_params[-1][1]**2)
		rad = np.sqrt(rk_params[2][0]**2 + rk_params[2][1]**2)
		esc_vel = np.sqrt(2 * G * red_mass / rad)

		# If the planet has been, stop the loop
		if vel >= (3*esc_vel):
			final_time = tt
			print("Velocity end")
			break

	# If the planet has been flung out, cut the arrays short so that they can be
	# plotted.
	if final_time != 0:
		xpts_s1 = xpts_s1[:final_time]
		ypts_s1 = ypts_s1[:final_time]

		xpts_s2 = xpts_s2[:final_time]
		ypts_s2 = ypts_s2[:final_time]

		xpts_p = xpts_p[:final_time]
		ypts_p = ypts_p[:final_time]

	# Plotting
	fig, ax = plt.subplots()
	ax.set_xlabel("AU")
	ax.set_ylabel("AU")
	ax.set_title("Stars {0} AU Apart, Planet {1} AU Away".format(A, test_plan))
	ax.plot(xpts_s1, ypts_s1, label="Star 1")
	ax.plot(xpts_s2, ypts_s2, label="Star 2")
	ax.plot(xpts_p, ypts_p, label ="Planet")
	plt.legend(loc="best")
	if final_time != 0:	
		plt.savefig("Fail_for_{0}_star_{1}_planet".format(A, test_plan))
	else:
		plt.savefig("Possible_for_{0}_star_{1}_planet".format(A, test_plan))
	plt.show()
