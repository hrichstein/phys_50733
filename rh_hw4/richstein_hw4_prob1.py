"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 4, Problem 1 - Radioactive Decay
Last edited: 22 February 2017

Overview:
---------


Input:
------


Output:
-------


"""

from random import random
from numpy import arange
from matplotlib import pyplot as plt


N_213_bi = 10000					 # the number of atoms we begin with
N_209_tl = 0
N_209_pb = 0
N_209_bi = 0


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

tpoints = arange(0.0, tmax, h)

bi_213pts = [[] for tt in range(len(tpoints))]
tl_209pts = [[] for tt in range(len(tpoints))]
pb_209pts = [[] for tt in range(len(tpoints))]
bi_209pts = [[] for tt in range(len(tpoints))]


for tt in range(len(tpoints)):
	bi_213pts[tt] = N_213_bi
	tl_209pts[tt] = N_209_tl
	pb_209pts[tt] = N_209_pb
	bi_209pts[tt] = N_209_bi

	if N_209_tl > 0:
		print("Bi 213 = {}".format(N_213_bi))
		print("Tl 209 = {}".format(N_209_tl))
		print("Pb 209 = {}".format(N_209_pb))
		print("Bi 209 = {}".format(N_209_bi))

	dec_to_pb = 0
	decay = 0
	for ii in range(N_213_bi):
		if random() < p_213_bi:
			decay += 1
			if random() < p_pb_over_tl:
				dec_to_pb += 1
	N_213_bi -= decay
	N_209_pb += dec_to_pb
	N_209_tl += (decay - dec_to_pb)

	decay = 0
	for ii in range(N_209_tl):
		if random() < p_209_tl:
			decay += 1
	N_209_tl -= decay
	N_209_pb += decay

	decay = 0
	for ii in range(N_209_pb):
		if random() < p_209_pb:
			decay += 1
	N_209_pb -= decay
	N_209_bi += decay

fig, ax = plt.subplots()
ax.plot(tpoints, bi_213pts, label="213 Bi")
ax.plot(tpoints, tl_209pts, label="209 Tl")
ax.plot(tpoints, pb_209pts, label="209 Pb")
ax.plot(tpoints, bi_209pts, label="209 Bi")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Number of Atoms")
ax.legend()

plt.tight_layout()
plt.show()
