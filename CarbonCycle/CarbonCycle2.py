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

def F(i, j):
	if i == 4 and j == 1:
		return (k[4][1]*N[4]*(1 + beta*np.log(N[1] / originalN[1])))
	elif i == 1 and j == 2:
		return (k[2][1]*(originalN[1] + ((originalN[1] / originalN[2])*(N[2] - originalN[2]))))
	else:
		return (k[i][j] * N[j])

def deltaN1():
	return (F(1, 2) + F(1, 4) + F(1, 7) + F(1, 6) - F(2, 1) - F(4, 1))

def deltaN2():
	return (F(2, 3) + F(2, 1) - F(1, 2) - F(3, 2))

def deltaN3():
	return (F(3, 2) - F(2, 3))

def deltaN4():
	return (F(4, 1) - F(1, 4) - F(6, 4) - F(5, 4))

def deltaN5():
	return (F(5, 4) - F(6, 5))

def deltaN6():
	return (F(6, 4) + F(6, 5) - F(7, 6) - F(1, 6))

def deltaN7():
	return (F(7, 6) - F(1, 7))

# constants
deltaT = 0.1
t = 0
burned = False
beta = 0.1
originalN = ['placeholder', 700, 1000, 36000, 130, 700, 60, 1500]

N = ['placeholder', 700, 1000, 36000, 130, 700, 60, 1500]

# kij's are the original always equilibrium numbers? or are they initial values?
k = np.empty((8, 8))
k[2][1] = 100 / originalN[1]
k[1][2] = 100 / originalN[2]
k[3][2] = (100 / 3) / originalN[2]
k[2][3] = (100 / 3) / originalN[3]
k[1][4] = 55 / originalN[4]
k[4][1] = 110 / 130
k[6][4] = 40 / originalN[4]
k[5][4] = 15 / originalN[4]
k[6][5] = 15 / originalN[5]
k[7][6] = 2 / originalN[6]
k[1][7] = 2 / originalN[7]
k[1][6] = 53 / originalN[6]

# make the arrays which will hold all the deltaN values which is what we will actually graph
x = np.arange(0, 100,  0.1)
N1array = np.empty(1000)
N2array = np.empty(1000)
N3array = np.empty(1000)
N4array = np.empty(1000)
N5array = np.empty(1000)
N6array = np.empty(1000)
N7array = np.empty(1000)
# they are all declared the same way to make exactly sure they are the same size

# now make the fancy for loop to do all the hard work
for i in range(0, 1000):
	if t >= 10 and not burned:
		N[1] += 10
		burned = True
	N1array[i] = deltaN1()
	N[1] = N[1] + (N1array[i]*deltaT)
	print('i:',i,'t:',t,'array:',N1array[i],'N1:', N[1])
	N2array[i] = deltaN2()
	N[2] = N[2] + (N2array[i]*deltaT)
	N3array[i] = deltaN3()
	N[3] = N[3] + (N3array[i]*deltaT)
	N4array[i] = deltaN4()
	N[4] = N[4] + (N4array[i]*deltaT)
	N5array[i] = deltaN5()
	N[5] = N[5] + (N5array[i]*deltaT)
	N6array[i] = deltaN6()
	N[6] = N[6] + (N6array[i]*deltaT)
	N7array[i] = deltaN7()
	N[7] = N[7] + (N7array[i]*deltaT)
	t += deltaT

plot(x,N1array)
plot(x,N2array)
plot(x,N3array)
plot(x,N4array)
plot(x,N5array)
plot(x,N6array)
plot(x,N7array)
axis([0, 100, -2, 2])
xlabel('Time')
ylabel('Change in container size')
show()