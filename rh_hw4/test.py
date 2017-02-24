from random import random
from numpy import arange
from matplotlib import pyplot as plt

N_213_bi = 100
N_209_tl = 0
N_209_pb = 0

tmax = 1000
h = 1.0  # size of time step in seconds


tau_213_bi = 46 * 60  # half-life of Bi 213 in seconds
p_213_bi = 1 - 2**(-h / tau_213_bi)

p_pb_over_tl = 0.9791

tpoints = arange(0.0, tmax, h)

bi_213pts = [[] for tt in range(len(tpoints))]
tl_209pts = [[] for tt in range(len(tpoints))]
pb_209pts = [[] for tt in range(len(tpoints))]
bi_209pts = [[] for tt in range(len(tpoints))]


for tt in range(len(tpoints)):
	bi_213pts[tt] = N_213_bi
	tl_209pts[tt] = N_209_tl
	pb_209pts[tt] = N_209_pb

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

fig, ax = plt.subplots()
ax.plot(tpoints, bi_213pts, label="213 Bi")
ax.plot(tpoints, tl_209pts, label="209 Tl")
ax.plot(tpoints, pb_209pts, label="209 Pb")

ax.set_xlabel("Time (s)")
ax.set_ylabel("Number of Atoms")
ax.legend()

plt.tight_layout()
plt.show()