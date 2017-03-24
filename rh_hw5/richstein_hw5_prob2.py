"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 5, Problem 2 - Data Fitting: SDSS
Last edited: 24 March 2017

Overview:
---------
This program intakes data from SDSS Data Release 13 and tries to fit a linear, quadratic, and broken linear function to the magnitude vs redshift relation.

Input:
------
The specObj .fits file from SDSS DR-13

Output:
-------
Prints best-fit values for the parameters and the responses to questions on the assignment sheet. Saves the plot as a .png file and then plots it to the screen.

"""

import fitsio
import numpy as np
from scipy.optimize import curve_fit
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

#Sorting out data with acceptable bitmasks and the magnitude limit as given by http://www.sdss.org/dr13/scope/
#This creates an array of indices where the two conditions are true
good_ind= data[1].where("ZWARNING == 0 && 22.5 - (2.5 * log10(SPECTROFLUX[3])) <= 22.2")

#Then apply these indices when creating the initial z_err, spectroflux, and z arrays
z_err_arr = data[1]["Z_ERR"][good_ind]
spflux_1 = data[1]["SPECTROFLUX"][good_ind]
z_arr_1 = data[1]["Z"][good_ind]

#Filtering out objects without a "reasonable" z_err value.
z_err_reason = np.logical_and(z_err_arr < 1,z_err_arr > 0)

#Applying the above truth table to the three arrays
z_err_arr = z_err_arr[z_err_reason]
spflux_2 = spflux_1[z_err_reason]
z_arr_2 = z_arr_1[z_err_reason]

#Converting from nanomaggies
SP_FLUX_convert = 22.5 - (2.5 * np.log10(spflux_2))

#Finding the appropriate induces
SP_cut = np.logical_and((SP_FLUX_convert[:,3]-SP_FLUX_convert[:,4]) > 0.6, (SP_FLUX_convert[:,3]-SP_FLUX_convert[:,4]) < 0.65)

#Slicing out the data we want
z_err_arr = z_err_arr[SP_cut]
SP_FLUX_subset = SP_FLUX_convert[SP_cut]
z_arr_3 = z_arr_2[SP_cut]

####One more layer of filtering the data which uses the mean and standard deviation of the z_err values to restrict which points are taken into consideration. The max error it allows is around 0.043. Incidentally, this only ends up removing 50 or so points, but it drastically changes the best-fit models.
# z_err_good = np.logical_and( abs(z_err_arr) <= (3*np.std(z_err_arr) + np.mean(z_err_arr)),abs(z_err_arr) >= (-3*np.std(z_err_arr) + np.mean(z_err_arr)))

# SP_FLUX_array = SP_FLUX_subset[z_err_good]
# z_arr = z_arr_2[z_err_good]
# z_err_arr = z_err_arr[z_err_good]

# SP_flux_3 = SP_FLUX_array[:,3]

#Taking the third column of the data (the r-band)
SP_flux_3 = SP_FLUX_subset[:,3]
z_arr = z_arr_3

#Defining the functions to be used in curve-fit
def line(x,slope,intercept):
	return slope * x + intercept

def quad(x,a,b,intercept):
	return a * x**2 + b*x + intercept

def broken(xvals,x,y):
	return np.interp(xvals, x, y)

popt, pcov = curve_fit(line, z_arr, SP_flux_3,sigma=z_err_arr)

print("\na)\n")
print("Best-Fit Values - Linear:\n")
print("Slope: {0:.2f}".format(popt[0]))
print("Intercept: {0:.2f}".format(popt[1]))

popt2, pcov2 = curve_fit(quad, z_arr, SP_flux_3,sigma=z_err_arr)

print("\nBest-Fit Values - Quadratic:\n")
print("Quadratic Coefficient: {0:.2f}".format(popt2[0]))
print("Linear Coefficient: {0:.2f}".format(popt2[1]))
print("Constant: {0:.2f}".format(popt2[2]))

#There are no best-fit values for the broken linear fit using the interp method.

print("\nb)\n")
print("None of these functions fits very well, but from the three, the broken linear is probably the best. The data is certainly not linear, and the quadratic is not following the trend we could expect. We would want this to curve upwards, so objects at higher redshift would have higher magnitudes. When trying different methods of filtering the data, there was a way to have the quadratic curve the other way, but then the linear fit had a negative slope. That was done by further restricting the allowed z_err values.")

xvals = np.linspace(min(z_arr),max(z_arr),3*(max(z_arr)-min(z_arr)))

broken_y_fit = broken(xvals,z_arr,SP_flux_3)

fig, ax = plt.subplots()

ax.errorbar(z_arr,SP_flux_3,xerr=z_err_arr,fmt='None')
ax.plot(np.sort(z_arr),popt[0]*np.sort(z_arr)+popt[1],label="Linear",linewidth=2)
ax.plot(np.sort(z_arr),popt2[0]*np.sort(z_arr)**2 + popt2[1]*np.sort(z_arr)+popt2[2],label="Quadratic",linewidth=2)
ax.plot(xvals,broken_y_fit,label="Broken Linear",linewidth=2)

ax.set_ylabel(r"r-band Magnitude",size=va.size_ylabel)
ax.set_xlabel("Redshift",size=va.size_xlabel)
ax.set_xlim(-0.01,max(z_arr)+0.25)
ax.set_ylim(14,max(SP_flux_3)+0.25)
ax.tick_params(axis='both', which='major', labelsize=va.size_tick)

plt.legend(loc="best")
plt.tight_layout()
# plt.savefig("richstein_hw5_prob2_plot",format="png")
plt.show()