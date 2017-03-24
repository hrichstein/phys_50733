

from numpy import cos, pi, genfromtxt, array, mean, where, std, logical_and
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from matplotlib import rc,rcParams
# rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')

rc('font', **{'family': 'serif', 'serif':['Computer Modern']})


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
guess_amp = 25 # from looking at plot
guess_phase = 0
guess_offset = mean(temp_good)

#Initial parameter array
p0 = array([guess_amp, guess_phase, guess_offset])

#Using curve fit to find best parameters
fit = curve_fit(my_cos, year_good, temp_good, p0 = p0)

#Using the optimized parameters in my cosine function
data_fit = my_cos(year_good, *fit[0])

###PLOTTING
fig, ax = plt.subplots(figsize=(14,5))

ax.plot(year_good,temp_good, label="Good data")
ax.plot(year_good,data_fit, label="Best-Fit Model")
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.set_xlim(min(year_good),max(year_good))
ax.set_ylabel(r"Temperature (C $\degree$)")
ax.set_xlabel("Year")

plt.legend()
plt.tight_layout()
plt.show()

##END PROGRAM