This subdirectory contains 2 homework problems and their outputs in .txt and 
.png files.

**Code for Problem 1**

This program performs a data fit on the daily average temperatures of Munich.
It relies on the scipy.optimize curve_fit function to find the best-fit values.
parameters.

*Output for Problem 1*

A .txt file containing the best-fit values for the parameters and the answers to the questions posed on the assignment sheet.

A .png file showing the plots of the masked data and the best-fit model.

**Code for Problem 2**

This program intakes data from SDSS Data Release 13 and tries to fit a linear, quadratic, and broken linear function to the magnitude vs redshift relation.

*Output for Problem 2*

A .txt file containing the best-fit values for the parameters and the answers to the questions posed on the assignment sheet. (Note: There were no best-fit values found for the broken linear fit, as I used the numpy.interp function.)

A .png file showing the plots of the selected data and the best-fit models.

A .png file (zoomed) showing a restricted y-range in version of the main plot.