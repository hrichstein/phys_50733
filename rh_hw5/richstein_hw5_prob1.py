

from numpy import cos, pi, genfromtxt, array, mean, where, std, logical_and
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# weather_fit(t) = a * cos(2*pi*t + b) + C

munich_temps = array(genfromtxt("munich_temperatures_average_with_bad_data.txt",
	usecols=[0,1],unpack=True))

def my_cos(x, freq, amplitude, phase, offset):
	return cos(x * freq + phase) * amplitude + offset

year = munich_temps[0]
temp = munich_temps[1]

yr_small_range = year[logical_and(year >= 2008,year<2013)]  # To include the year 2012
temp_small_range = temp[logical_and(year >= 2008,year<2013)] 

year = yr_small_range
temp = temp_small_range

temp_good = temp[abs(temp) < (3 * std(temp) + mean(temp))]
year_good = year[abs(temp) < (3 * std(temp) + mean(temp))]


freq = 2 * pi

guess_amp = 25 # from looking at plot
guess_phase = 0
guess_offset = mean(temp_good)

p0 = array([freq, guess_amp, guess_phase, guess_offset])

fit = curve_fit(my_cos, year_good, temp_good, p0 = p0)

# data_first_guess = my_cos(temp_good, *p0)

data_fit = my_cos(year_good, *fit[0])


fig, ax = plt.subplots()

ax.plot(year_good,temp_good)
ax.plot(year_good,data_fit, label="after fitting")

ax.set_xlim(min(year_good),max(year_good))
ax.set_ylabel(r"Temperature (C $\degree$)")
ax.set_xlabel("Year")
# plt.plot(year_good, data_first_guess, label="first guess")
plt.legend()
plt.tight_layout()
plt.show()

###
#np.logical_and(a>1,a<5) -> only takes two arguments

## 1 year 