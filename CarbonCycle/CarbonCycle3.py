# Calculates and outputs carbon cycle data based on Bolin's model
# 7 different "Containers": Atmosphere, Mixed Upper Ocean Layer, Deep Ocean Layer, Short-lived Terrestrial Biota, Long-lived Biota, Detritus, Soil
# respectively they are: N1, N2, N3, N4, N5, N6, N7
# relationships between different containers are described by Fij where carbon flows to compartment i from compartment j
# from i to j
# Equilibrium values: 
# 	N1 = 700
# 	N2 = 1000
# 	N3 = 36000
# 	N4 = 130
# 	N5 = 700
# 	N6 = 60
# 	N7 = 1500
# where units are 10^15 grams (a gigaton; GT), Transfers are in GT/year

import numpy as np
from matplotlib.pylab import *

# function for getting Fij = kij*Nj, exceptions are in F41 and F12
def F(i, j):
	if i == 4 and j == 1:
		return (k[4][1]*N[4]*(1 + beta*logi(N[1] / 700)))
	elif i == 1 and j == 2:
		return (N[2] - 900)
	else:
		return (k[i][j] * N[j])

# gets new value for container, Euler's Method
def newCont(N, container):
	N[container] = N[container] + (deltas[container]() * deltaT)
	return

# This a dictionary which allows look up of a lambda function based on the N number
deltas = { 1: lambda : (F(1, 2) + F(1, 4) + F(1, 7) + F(1, 6) - F(2, 1) - F(4, 1)),
			2: lambda : (F(2, 3) + F(2, 1) - F(1, 2) - F(3, 2)),
			3: lambda : (F(3, 2) - F(2, 3)),
			4: lambda : (F(4, 1) - F(1, 4) - F(6, 4) - F(5, 4)),
			5: lambda : (F(5, 4) - F(6, 5)),
			6: lambda : (F(6, 4) + F(6, 5) - F(7, 6) - F(1, 6)),
			7: lambda : (F(7, 6) - F(1, 7)),
		}

# ways to avoid using dot notation repeatedly because it introduces inefficiencies
logi = np.log
empties = np.empty

# constants
deltaT = 0.1
beta = 0.1
legends = ['Atmosphere', 'Mixed Upper Ocean Layer', 'Deep Ocean Layer', 'Short-lived Terrestrial Biota', 'Long-lived Biota', 'Detritus', 'Soil']
labelStr = 'Change in amount of Carbon (GT)'


# Original N values, N will change with each iteration, original doesn't change
N = ['placeholder', 700, 1000, 36000, 130, 700, 60, 1500]
original = ('placeholder', 700, 1000, 36000, 130, 700, 60, 1500) # tuple because its harder to change

# kij's are the original always equilibrium numbers
k = empties((8, 8))
k[2][1] = 100 / 700
k[1][2] = 100 / 1000
k[3][2] = (100 / 3) / 1000
k[2][3] = (100 / 3) / 36000
k[1][4] = 55 / 130
k[4][1] = 110 / 130
k[6][4] = 40 / 130
k[5][4] = 15 / 130
k[6][5] = 15 / 700
k[7][6] = 2 / 60
k[1][7] = 2 / 1500
k[1][6] = 53 / 60

# make the arrays which will hold all the difference from original values which is what we will actually graph
x = np.arange(0, 100,  0.1)
NGraphArrays = ['placeholder', empties(1000), empties(1000), empties(1000), empties(1000), empties(1000), empties(1000), empties(1000)]

# now make the fancy for loop to do all the hard work
for i in range(1, 1000):
	if i == 102: # 102 because 0.1 can't be stored in binary properly
		N[1] += 10 # increase carbon in atmosphere
	for j in range(1, 8):
		newCont(N, j) # get new amount of carbon in each container with euler's method
	for j in range(1, 8):
		NGraphArrays[j][i] = N[j] - original[j] # numbers to graph are how differnent current amount of carbon  is from original

# go through and plot each line on a graph
for i in range (1, 8):
	plot(x,NGraphArrays[i])

# add all the regular graph stuffs
xlabel('Time')
ylabel(labelStr)
legend(legends)
title('Variance in Carbon Levels After Introduction of a Large Amount of Carbon')
axis([0, 100, -10, 10])
grid(True)
axhline(0, color='black', lw=2)
axvline(0, color='black', lw=2)
show()