"""

Student Name: Hannah Richstein
Professor Name: Dr. Frinchaboy
Class: PHYS 50733
In-Class, 6 February 2017
Last edited: 6 Feb 2017

Overview:
---------
This program employs two methods of Simpson's rule to find the integral for the
given function, f(x).

Input:
------
N/A

Output:
-------
Two values of the integral as calculated by two separate summation equations.

Program Limitations:
--------------------
Python precision, using computers to perform integration

Significant Program Variables:
------------------------------
N = upper limit of summation

a = lower integration limit

b = upper integration limit

h = step-size

"""

#Defining the function to be integrated
def f(x):
	return x**4 - (2*x) + 1

#Declaration of Constants
N = 10
a = 0.0
b = 2.0
h = (b - a) / N
###############################################################################
#5.9 Version of Simpson's Rule'

#Calculating the first summation term
first_sum = 0.0
for k in range(1,N,2):
	first_sum += f(a + (k*h))
	# print("k={0}".format(k))
	# print("First Sum = {0}".format(first_sum))

#Calculating the second summation term
second_sum = 0.0
for k in range(2,N,2):
	second_sum += f(a + (k*h))
	# print("k={0}".format(k))
	# print("Second Sum = {0}".format(second_sum))

#Combing all terms in the summation, in multiple steps to see whether improper
#syntax was affecting my answer
int_1 = f(a) + f(b)
int_2 = 4*first_sum
int_3 = 2*second_sum

int_4 = int_1 + int_2 + int_3

int_5 = (h/3)*int_4
print("Eq. 5.9 Version:")
print(int_5)

###############################################################################
#5.10 Version of Simpson's Rule

#Calculating the first summation term
first_sum = 0.0
for k in range(1,int(N/2)+1,1):
	first_sum += f(a + ( (2*k - 1)*h ) )
	# print("k={0}".format(k))
	# print("First Sum = {0}".format(first_sum))

#Calculating the second summation term
second_sum = 0.0
for k in range(1,int(N/2 -1)+1,1):
	second_sum += f(a + (2*k*h) )
	# print("k={0}".format(k))
	# print("Second Sum = {0}".format(second_sum))

#Combining the terms all in one line, also seeing if it would affect the answer
integral = (1/3) * h * ( f(a) + f(b) + (4*first_sum) + (2*second_sum) )

print("")
print("Eq. 5.10 Version:")
print(integral)

#END PROGRAM