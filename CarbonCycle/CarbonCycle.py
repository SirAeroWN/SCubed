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

# Atmosphere->Mixed Upper Ocean Layer; Eflow = 100
def F21():
	return (k21 * N1)

# Mixed Upper Ocean Layer->Atmosphere; Eflow = 100
def F12():
	return (k21*(originalN1 + ((originalN1 / originalN2)*(N2 - originalN2))))

# Mixed Upper Ocean Layer->Deep Ocean Layer; Eflow = 100/3
def F32():
	return (k32 * N2)

# Deep Ocean Layer->Mixed Upper Ocean Layer; Eflow = 100/3
def F23():
	return (k23 * N3)

# Short-lived Terrestrial Biota->Atmosphere; Eflow = 55
def F14():
	return (k14 * N4)

# Atmosphere->Short-lived Terrestrial Biota; Eflow = 110
def F41():
	return (k41*N4*(1 + beta*np.log(N1 / originalN1)))

# Short-lived Terrestrial Biota->Detritus; Eflow = 40
def F64():
	return (k64 * N4)

# Short-lived Terrestrial Biota->Long-lived Biota; Eflow = 15
def F54():
	return (k54 * N4)

# Long-lived Biota->Detritus; Eflow = 15
def F65():
	return (k65 * N5)

# Detritus->Soil; Eflow = 2
def F76():
	return (k76 * N6)

# Soil->Atmosphere; Eflow = 2
def F17():
	return (k17 * N7)

# Detritus->Atmosphere; Eflow = 53
def F16():
	return (k16 * N6)

def deltaN1():
	return (( -1 * F21()) - F41() + F12() + F14() + F17() + F16())

def deltaN2():
	return (( -1 * F12()) - F32() + F23() + F21())

def deltaN3():
	return (( -1 * F23()) + F32())

def deltaN4():
	return (( -1 * (F14()) - F64() - F54() + F41()))

def deltaN5():
	return (( -1 * F65()) + F54())

def deltaN6():
	return (( -1 * F76()) - F16() + F64() + F65())

def deltaN7():
	return (( -1 * F17()) + F76())

# constants
deltaT = 0.1
beta = 0.1
originalN1 = 700
originalN2 = 1000
originalN3 = 36000
originalN4 = 130
originalN5 = 700
originalN6 = 60
originalN7 = 1500

N1 = 700
N2 = 1000
N3 = 36000
N4 = 130
N5 = 700
N6 = 60
N7 = 1500

# kij's are the original always equilibrium numbers? or are they initial values?
k21 = 100 / originalN1
k12 = 100 / originalN2
k32 = (100 / 3) / originalN2
k23 = (100 / 3) / originalN3
k14 = 55 / originalN4
k41 = 110 / 130
k64 = 40 / originalN4
k54 = 15 / originalN4
k65 = 15 / originalN5
k76 = 2 / originalN6
k17 = 2 / originalN7
k16 = 53 / originalN6

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
	N1array[i] = deltaN1()
	N1 = N1 + (N1array[i]*deltaT)
	print(N1array[i])
	N2array[i] = deltaN2()
	N2 = N2 + (N2array[i]*deltaT)
	N3array[i] = deltaN3()
	N3 = N3 + (N3array[i]*deltaT)
	N4array[i] = deltaN4()
	N4 = N4 + (N4array[i]*deltaT)
	N5array[i] = deltaN5()
	N5 = N5 + (N5array[i]*deltaT)
	N6array[i] = deltaN6()
	N6 = N6 + (N6array[i]*deltaT)
	N7array[i] = deltaN7()
	N7 = N7 + (N7array[i]*deltaT)

plot(x,N1array)
plot(x,N2array)
plot(x,N3array)
plot(x,N4array)
plot(x,N5array)
plot(x,N6array)
plot(x,N7array)
axis([0, 100, 0, 10000])
xlabel('Time')
ylabel('Change in container size')
show()