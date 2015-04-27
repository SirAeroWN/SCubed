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

# Atmosphere->Mixed Upper Ocean Layer; Eflow = 100
def F21():
	return

# Mixed Upper Ocean Layer->Atmosphere; Eflow = 100
def F12():
	return

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
	return

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