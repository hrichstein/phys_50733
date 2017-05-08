"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
Project: Double Stars Planetary System
Last edited: 8 May 2017

Overview:
---------
This program calculates and plots the orbits/motions for the three-body system
consisting of two binary stars of 1 solar mass and a planet with 1 Earth mass.

Input:
------
The user is asked for the distance separating the binary stars, the first guess
for where the planet should begin, the last guess for which its orbit should be
calculated, and the distance between each orbit which will be calculated. The
user is also able to specify whether s/he wants the planet to begin on the x-
axis (on the same line as the stars) or y-axis (perpendicular).

Output:
-------
This will print to the terminal screen a description of the case being
investigated, the period and initial velocity for the stars and planet, and the
energy coefficient which should be multiplied by the mass of the Earth to
determine the 

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

	print("\nPeriod is {0:.3f} years".format(period))

	v = np.sqrt(G * Mc * (2-1)/a)

	print("Initial velocity: {0:.2f} AU/years".format(v))

	# print(2*np.pi*a/v) Check for whether the circumference divided by the
	# velocity actually gave me the period found above

	return period, v

def find_vel_tight(Ms, s, p):
	"""
	This function is specifically for when the planet is orbiting one of the
	stars (in a fairly tight orbit, hence the name). 

	Parameters
	----------
	Ms: float-like
		Mass of the star the planet is orbiting

	s: array-like
		x, y position of the star

	p: array-like
		x, y position of the planet

	Output
	------
	v: float-like
		Velocity which the planet should initially be going if it is to
		complete an orbit in the period solved for using Newton's version
		of Kepler's third law

	"""

	dist = np.sqrt((s[0]-p[0])**2 +(s[1]-p[1]))

	period = np.sqrt(4 * np.pi**2 * dist**3 / G / (Ms)) # period in years

	print("\nPeriod is {0:.3f} years".format(period))

	v = np.sqrt(G * Ms * (2-1)/dist)

	print("Initial velocity: {0:.2f} AU/years".format(v))

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
A = float(input("Please input the distance between the two stars in AU: "))
r = A/2  # semi-major axis & radius of circle they will be orbiting

# Taking user input to define which planet positions will be used.
intake = [ii for ii in input("\nPlease input the first separation distance from "
	+ "the center of mass\nyou would like the planet to start at, \n"
	+ "the last separation distance you would like to try, and the step size, "
	+ "\nall in AU and separated by commas. \nAlso, please type x or y to "
	+ "specify whether you would like the planet \nto begin on a line parallel "
	+ "or perpendicular to the two stars: ").split(',')]

start = float(intake[0])
stop = float(intake[1])
step = float(intake[2])
x_y_flag = str(intake[3])

test_plan_arr = np.arange(start, stop+step, step, dtype=float)

# Mass Settings
M1 = 1  # solar mass
M2 = 1  # solar mass

red_mass = M1*M2/(M1+M2)  # Reduced mass (solar)

possible = 0
p_around_s = 0

for xx in test_plan_arr:

	test_plan = xx  # AU

	print("\n------------------------------------------------------------------"
		+"------------------------")
	print("Case for Binary Stars separated by {0} AU and planet starting at "
		+"{1} AU from center of mass.".format(A, test_plan))
	print("\n------------------------------------------------------------------"
		+"------------------------")


	if (abs(A/2-start) < (0.5 * A)):
		p_around_s = 1
		print("\n*********************************")
		print("Planet is orbiting a single star.")
		print("*********************************")

	# Initial conditions
		# Positions
	s1 = np.array([r, 0], float)
	s2 = np.array([-r,0], float)

	if "x" in x_y_flag:
		p = np.array([test_plan, 0], float)
	else:
		p = np.array([0, test_plan], float)

	# Calculating initial velocities
	print("\nFor Stars:")
	s_period, s_vel = find_vel_init(red_mass, r)

	print("\nFor Planet:")
	if p_around_s:
		p_period, p_vel = find_vel_tight(M1, s1, p)
		center_bod = M1
	else:		
		p_period, p_vel = find_vel_init(red_mass, test_plan)
		center_bod = red_mass

		# Velocities
	s1_v0 = np.array([0, s_vel], float)
	s2_v0 = np.array([0, -s_vel], float)

	if "x" in x_y_flag:
		p_v0 = np.array([0, p_vel], float)
	else:
		p_v0 = np.array([p_vel, 0], float)

	E = (0.5*p_vel**2) - (G*center_bod/test_plan)
	print("\nEnergy coefficient (to be multiplied by Earth mass): {0:.2f} AU^2/yr^2".format(E))

	# Setting the length of time the program will run based on whether the planet
	# will be orbiting both stars or just one.
	if p_around_s:
		end_time = 1.5 * s_period
	elif A > 150:
		end_time = 5 * p_period
	else:
		end_time = 1.25 * p_period

	# Trying to set an acceptable number of steps that won't be overkill 
	# considering the length of the period
	if end_time < 1000:
		step_num = 1e5
	elif end_time < 5000:
		step_num = 5e5
	else:
		step_num = 1e6

	# Time setup
	a = 0
	b = end_time
	N = step_num
	h = (b-a)/N

	tpoints = np.arange(a, b, h, dtype=int)	


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

		# Checking to see if the planet has been flung off yet
		vel = np.sqrt(rk_params[-1][0]**2 + rk_params[-1][1]**2)
		rad = np.sqrt(rk_params[2][0]**2 + rk_params[2][1]**2)
		esc_vel = np.sqrt(2 * G * red_mass / rad)

		# If the planet has been, stop the loop
		if A < 100:
			if vel >= (3*esc_vel):
				final_time = tt
				if final_time == 0:
					final_time += 1
				print("Escape velocity limit reached.")
				break
		else:
			if vel >= (15*esc_vel):
				final_time = tt
				if final_time == 0:
					final_time += 1
				print("Escape velocity limit reached.")
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
		plt.savefig("Fail_for_{0}_star_{1}_planet.png".format(A, test_plan))
	else:
		plt.savefig("Possible_for_{0}_star_{1}_planet.png".format(A, test_plan))
		possible += 1
	plt.show()

	if possible >= 6:
		print("Have generated 6 possible stable orbits.")
		break
