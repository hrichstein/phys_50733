"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
HW 5, Problem 1 - Data Fitting: Munich Temperatures
Last edited: 24 March 2017

Overview:
---------
This program performs a data fit on the daily average temperatures of Munich.
It relies on the scipy.optimize curve_fit function to find the best-fit values.
parameters.

Input:
------
Takes in the file munich_temperatures_average_with_bad_data.txt

Output:
-------
Prints best-fit values for the parameters and the responses to questions on the assignment sheet. Saves the plot as a .png file and then plots it to the screen.

"""

from numpy import cos, pi, genfromtxt, array, mean, where, std, logical_and
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

#Importing data
munich_temps = array(genfromtxt("munich_temperatures_average_with_bad_data.txt",
	usecols=[0,1],unpack=True))

#Defining the function which I will use to fit the temperature pattern
def my_cos(t, amplitude, phase, offset):
	return cos(t * 2 * pi + phase) * amplitude + offset

#Separating the data into the year and temperature
year = munich_temps[0]
temp = munich_temps[1]

#Picking out just the year range specified
yr_small_range = year[logical_and(year >= 2008,year<2013)]  # To include the year 2012
temp_small_range = temp[logical_and(year >= 2008,year<2013)] 

#This step to prevent a mix-up of indices above
year = yr_small_range
temp = temp_small_range

#Using standard deviation from the mean to mask out bad data
temp_good = temp[logical_and((abs(temp) < (3 * std(temp) + mean(temp))),
	(abs(temp) > (-3 * std(temp) + mean(temp))))]
year_good = year[logical_and((abs(temp) < (3 * std(temp) + mean(temp))),
	(abs(temp) > (-3 * std(temp) + mean(temp))))]

#Initial guesses for curve_fit routine
guess_amp = (max(temp_good) - min(temp_good)) / 2
guess_phase = 0
guess_offset = mean(temp_good)

#Initial parameter array
p0 = array([guess_amp, guess_phase, guess_offset])

#Using curve fit to find best parameters
fit = curve_fit(my_cos, year_good, temp_good, p0 = p0)

print("a)\n")
print("Best-Fit Values:\n")
print("Amplitude: {0:.2f}".format(fit[0][0]))
print("Phase: {0:.2f}".format(fit[0][1]))
print("Offset: {0:.2f}\n".format(fit[0][2]))

#Using the optimized parameters in my cosine function
data_fit = my_cos(year_good, *fit[0])

print("b)\n")
print("Overall Average Temperature: {0:.2f} degrees Celsius".format(mean(data_fit)))
print("Coldest Daily Average Temperature: {0:.2f} degrees Celsius".format(min(data_fit)))
print("Hottest Daily Average Temperature: {0:.2f} degrees Celsius".format(max(data_fit)))

print("c\n")
print("The b parameter is the horizontal shift of the cosine function. If the shift were zero, we'd be assuming the minimum temperature occurred on January 1st of every year. This isn't quite true, though we know it probably occurs sometime around there, so the shift shouldn't be too large. The value here makes sense, and suggests the minimum temperature occurs a short time after January 1st.")

###PLOTTING
fig, ax = plt.subplots(figsize=(14,5.5))

ax.plot(year_good,temp_good, label="Good data")
ax.plot(year_good,data_fit, label="Best-Fit Model")
ax.set_xlim(min(year_good),max(year_good))
ax.set_ylabel(r"Temperature ($\degree$C)",size=va.size_ylabel)
ax.set_xlabel("Year",size=va.size_xlabel)
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.tick_params(axis='both', which='major', labelsize=va.size_tick)

plt.legend(loc="best")
plt.tight_layout()
plt.savefig("richstein_hw5_prob1_plot",format="png")
plt.show()


##END PROGRAM
