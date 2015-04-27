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

# Atmosphere->Mixed Upper Ocean Layer; Eflow = 100
def F21():
	return

# Mixed Upper Ocean Layer->Atmosphere; Eflow = 100
def F12():
	return (k21*(originalN1 + ((originalN1 / originalN2)*(N2 - originalN2))))

# Mixed Upper Ocean Layer->Deep Ocean Layer; Eflow = 100/3
def F32():
	return

# Deep Ocean Layer->Mixed Upper Ocean Layer; Eflow = 100/3
def F23():
	return

# Short-lived Terrestrial Biota->Atmosphere; Eflow = 55
def F14():
	return

# Atmosphere->Short-lived Terrestrial Biota; Eflow = 110
def F41():
	return (k41*N4*(1 + beta*np.log(N1 / originalN1)))

# Short-lived Terrestrial Biota->Detritus; Eflow = 40
def F64():
	return

# Short-lived Terrestrial Biota->Long-lived Biota; Eflow = 15
def F54():
	return

# Long-lived Biota->Detritus; Eflow = 15
def F65():
	return

# Detritus->Soil; Eflow = 2
def F76():
	return

# Soil->Atmosphere; Eflow = 2
def F17():
	return

# Detritus->Atmosphere; Eflow = 53
def F16():
	return

def newY():
	return

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

k21 = F21() / originalN1
k12 = F12() / originalN2
k32 = F32() / originalN2
k23 = F23() / originalN3
k14 = F14() / originalN4
k41 = F41() / originalN1
k64 = F64() / originalN4
k54 = F54() / originalN4
k65 = F65() / originalN5
k76 = F76() / originalN6
k17 = F17() / originalN7
k16 = F16() / originalN6