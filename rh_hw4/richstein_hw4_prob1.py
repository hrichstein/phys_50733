"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 4, Problem 1 - Radioactive Decay
Last edited: 22 February 2017

Overview:
---------
This script examines the decay of Bi 213 to Tl 209, Pb 209, and Bi 209.  It
uses random numbers to determine, according to a probability value reliant on
the half-life, whether each atom will decay during any given time interval.

Input:
------
None -
Program does need constants specified, such as beginning number of atoms of
each type, the half-lives of the isotopes, the time interval, and the length of
time the process will be allowed to occur.

Output:
-------
A plot showing the populations of the four isotopes as time progresses.
It will also save this plot.

"""

from random import random
from numpy import arange, array
from matplotlib import pyplot as plt


N_213_bi = 10000					 # the number of atoms we begin with
N_209_tl = 0
N_209_pb = 0
N_209_bi = 0

output_arr = array([N_213_bi,N_209_tl,N_209_pb,N_209_bi])

tmin = 0
tmax = 20000  						 # the number of time steps to be taken
h = 1.0  							 # size of time step in seconds


tau_213_bi = 46 * 60  				 # half-life of Bi 213 in seconds
p_213_bi = 1 - 2**(-h / tau_213_bi)  # probability of Bi 213 atom decay


tau_209_tl = 2.2 * 60  				 # half-life of Tl 209 in seconds
p_209_tl = 1 - 2**(-h / tau_209_tl)  # probability of Tl 209 atom decay

tau_209_pb = 3.3 * 60  				 # half-life of Pb 209 in seconds
p_209_pb = 1 - 2**(-h / tau_209_pb)  # probability of Pb 209 atom decay

p_pb_over_tl = 0.9791  # probability when Bi 213 decays that it will decay to
					   # Pb 209 rather than Tl 209

tpoints = arange(0.0, tmax, h)		 # generating an array with time values

									 # generating empty lists to fill with
									 # the appropriate numbers of atoms
bi_213pts = [[] for tt in range(len(tpoints))]
tl_209pts = [[] for tt in range(len(tpoints))]
pb_209pts = [[] for tt in range(len(tpoints))]
bi_209pts = [[] for tt in range(len(tpoints))]

print("Time = (sec) [Bi 213,Tl 209,Pb 209,Bi 209]\n")
print("t = {:<6}".format(tmin) + "{0}".format(output_arr))

for tt in range(len(tpoints)):
	bi_213pts[tt] = N_213_bi		 # Assesing the number of each type of atom
	tl_209pts[tt] = N_209_tl		 # at the beginning of each time interval
	pb_209pts[tt] = N_209_pb
	bi_209pts[tt] = N_209_bi

	# if N_209_tl > 0:				 # Seeing that atoms do decay to Tl 209
	# 	print("Bi 213 = {}".format(N_213_bi))
	# 	print("Tl 209 = {}".format(N_209_tl))
	# 	print("Pb 209 = {}".format(N_209_pb))
	# 	print("Bi 209 = {}".format(N_209_bi))

	decay = 0						 # Decay trackers for the decay from Bi 213
	dec_to_pb = 0					 # and to Pb 209 specifically
	for ii in range(N_213_bi):		 # For each atom of Bi 213:
		if random() < p_213_bi:		 # Will it decay?
			decay += 1
			if random() < p_pb_over_tl:  # Since it's decaying, will it be Pb?
				dec_to_pb += 1
	N_213_bi -= decay
	N_209_pb += dec_to_pb
	N_209_tl += (decay - dec_to_pb)  # The number that decays to Tl should be
									 # the number of total atoms that decay
									 # minus the number which decay to Pb

	decay = 0						 # For those few that did decay to Tl 209,
	for ii in range(N_209_tl):
		if random() < p_209_tl:		 # will they decay to Pb 209?
			decay += 1
	N_209_tl -= decay
	N_209_pb += decay

	decay = 0						 # Now looking at the Pb 209,
	for ii in range(N_209_pb):
		if random() < p_209_pb:		 # how many will decay to Bi 209?
			decay += 1
	N_209_pb -= decay
	N_209_bi += decay

	output_arr = array([N_213_bi,N_209_tl,N_209_pb,N_209_bi])

	print("t = {:<7}".format(tt+1) + "{0}".format(output_arr))

fig, ax = plt.subplots()			 # Setting up plotting, then plotting
ax.plot(tpoints, bi_213pts, label="Bi 213")
ax.plot(tpoints, tl_209pts, label="Tl 209")
ax.plot(tpoints, pb_209pts, label="Pb 209")
ax.plot(tpoints, bi_209pts, label="Bi 209")

ax.set_xlabel("Time (s)")
ax.set_ylabel("Number of Atoms")
ax.set_title("Radioactive Decay of Bi 213")
ax.legend(loc="best")

plt.tight_layout()
plt.show()

plt.savefig("richstein_hw4_prob2_output.png")

# END PROGRAM
