"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 5, Problem 2 - Data Fitting: SDSS
Last edited: 24 March 2017

Overview:
---------


Input:
------


Output:
-------


"""

import fitsio
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import linregress
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from matplotlib import rc,rcParams
# rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')
rc('font', **{'family': 'serif', 'serif':['Computer Modern']})

class Vars(object):
    size_xlabel = 24
    size_ylabel = 24
    size_text   = 18
    size_tick   = 18

va = Vars()

data = fitsio.FITS("specObj-dr13.fits")

SP_FLUX_cut = data[1].where("((SPECTROFLUX[3]-SPECTROFLUX[4]) > 0.6) && ((SPECTROFLUX[3]-SPECTROFLUX[4]) < 0.65)")

subset_SP_flux = data[1][SP_FLUX_cut]["SPECTROFLUX"]

SP_flux_3 = np.transpose(subset_SP_flux)[3]
# SP_flux_4 = np.transpose(subset_SP_flux)[4]

# test_arr = SP_flux_3 - SP_flux_4

subset_z = data[1][SP_FLUX_cut]["Z"]
subset_z_err = data[1][SP_FLUX_cut]["Z_ERR"]


# slope, intercept, r_value, p_value, std_err = linregress(subset_z,SP_flux_3)

def line(x,slope,intercept):
	return slope * x + intercept

def quad(x,a,b,intercept):
	return a * x**2 + b*x + intercept

def broken(xvals,x,y):
	return np.interp(xvals, x, y)

popt, pcov = curve_fit(line, subset_z, SP_flux_3)

popt2, pcov2 = curve_fit(quad, subset_z, SP_flux_3)

xvals = np.linspace(min(subset_z),max(subset_z),3*(max(subset_z)-min(subset_z)))

test_y = broken(xvals,subset_z,SP_flux_3)

# popt3, pcov3 = curve_fit(broken,xvals, subset_z, SP_flux_3)

fig, ax = plt.subplots()

ax.plot(subset_z,SP_flux_3,".")
ax.plot(subset_z,popt[0]*subset_z+popt[1],label="linear")
ax.plot(subset_z,popt2[0]*subset_z**2 + popt2[1]*subset_z+popt2[2],label="quadratic")
ax.plot(xvals,test_y,label="Broken Linear")

plt.legend()
plt.show()