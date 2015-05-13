# dS/dt=((1-e*p)*u*N)-(B*I*S)-(u*S)
# dv/dt=e*p*u*N-u*V
# dI/dt=B*I*S-y*I-u*I
# dR/dt=y*I-u*R

import numpy as np
from matplotlib.pylab import *

def deltaS(Sp, Ip, e, p, u, N, B):
	return (((1 - (e * p)) * (u * N)) - (B * Ip * Sp) - (u * Sp))

def deltav(vp, e, p, u, N):
	return ((e * p * u * N) - (u * vp))

def deltaI(Ip, Sp, B, y, u):
	return ((B * Ip * Sp) - (y * Ip) - (u * Ip))

def deltaR(Rp, Ip, y, u):
	return ((y * Ip) - (u * Rp))

def newOverall(previous, deltaVal):
	return (previous + deltaVal)

def main():
	N = 183500000 # total population
	B = 0.00016123288 # force of infection
	u = (300000 / 183500000) #  death rate
	y = .5 # rate of recovery
	e = 0.365 # vaccine take, which is the fraction of vaccinated population who is protected by the vaccine
	p = 0.830076 # fraction of Nigeria’s population vaccinated at birth
	sarray = np.empty(50)
	varray = np.empty(50)
	iarray = np.empty(50)
	rarray = np.empty(50)
	sarray[0] = 183499900
	varray[0] = 0
	iarray[0] = 100
	rarray[0] = 0

	#print('s:', deltaS(S, I), '\nv:', deltav(v), '\nI:', deltaI(I, S), '\nR:', deltaR(R, I))

	for i in range(1, 50):
		ndS = deltaS(sarray[i - 1], iarray[i - 1], e, p, u, N, B)
		ndv = deltav(varray[i - 1], e, p, u, N)
		ndI = deltaI(iarray[i - 1], sarray[i - 1], B, y, u)
		ndR = deltaR(rarray[i - 1], iarray[i - 1], y, u)
		nS = newOverall(sarray[i - 1], ndS)
		nv = newOverall(varray[i - 1], ndv)
		nI = newOverall(iarray[i - 1], ndI)
		nR = newOverall(rarray[i - 1], ndR)
		if nS <= 0:
			nS = 0
		if nv <= 0:
			nv = 0
		if nI <= 0:
			nI = 0
		if nR <= 0:
			nR = 0
		sarray[i] = nS
		varray[i] = nv
		iarray[i] = nI
		rarray[i] = nR
		if iarray[i - 1] <= 0:
			iarray[i] = 0
		print('\n', i,'\n\ts:', sarray[i], '\n\tv:', varray[i], '\n\tI:', iarray[i], '\n\tR:', rarray[i])

	x = np.arange(0, 50, 1)

	plot(x, sarray)
	plot(x, varray)
	plot(x, iarray)
	plot(x, rarray)

	# add all the regular graph stuffs
	xlabel('Time (Years)')
	ylabel('Population ()')
	legend(['Susceptable', 'Vaccinated', 'Infected', 'Recovered'])
	title('Variance in Carbon Levels After Introduction of a Large Amount of Carbon')
	#axis([0, 50, 0, 300000])
	grid(True)
	axhline(0, color='black', lw=2)
	axvline(0, color='black', lw=2)
	show()

	plot(x, sarray)
	plot(x, varray)
	plot(x, iarray)
	plot(x, rarray)

	# add all the regular graph stuffs
	xlabel('Time (Years)')
	ylabel('Population ()')
	legend(['Susceptable', 'Vaccinated', 'Infected', 'Recovered'])
	title('Variance in Carbon Levels After Introduction of a Large Amount of Carbon')
	axis([0, 50, -4000000, 4000000])
	grid(True)
	axhline(0, color='black', lw=2)
	axvline(0, color='black', lw=2)
	#show()

main()