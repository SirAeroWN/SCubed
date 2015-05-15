# dS/dt=((1-e*p)*u*N)-(B*I*S)-(u*S)
# dv/dt=e*p*u*N-u*V
# dI/dt=B*I*S-y*I-u*I
# dR/dt=y*I-u*R

import numpy as np
from matplotlib.pylab import *
import tkinter as tk

def deltaS(Sp, Ip, e, p, u, N, B): # the change in susceptable population
	return (((1 - (e * p)) * (u * N)) - (B * Ip * Sp) - (u * Sp))

def deltav(vp, e, p, u, N): # change in vacinated population
	return ((e * p * u * N) - (u * vp))

def deltaI(Ip, Sp, B, y, u, k): # doesn't factor in people who die from being infected
	return ((B * Ip * Sp) - (y * Ip) - (u * Ip) - (k * Ip)) # now it does

def deltaR(Rp, Ip, y, u): # change in recovered population
	return ((y * Ip) - (u * Rp))

def newOverall(previous, deltaVal): # eulers method
	return (previous + deltaVal)

def main(Vars):
	# parse the list input
	N = float(Vars[0].get()) # total population
	B = float(Vars[1].get()) # force of infection
	u = float(Vars[2].get()) #  death rate
	y = float(Vars[3].get()) # rate of recovery
	e = float(Vars[4].get()) # vaccine take, which is the fraction of vaccinated population who is protected by the vaccine
	p = float(Vars[5].get()) # fraction of Nigeria’s population vaccinated at birth
	v = float(Vars[6].get()) # vaccinated population
	I = float(Vars[7].get()) # Infected population
	R = float(Vars[8].get()) # Recovered population
	k = float(Vars[9].get()) # death rate from malaria

	# declare arrays that will be used to graph
	sarray = empties(50)
	varray = empties(50)
	iarray = empties(50)
	rarray = empties(50)
	narray = empties(50)

	# initial values
	narray[0] = N
	sarray[0] = N - v - I - R
	varray[0] = v
	iarray[0] = I
	rarray[0] = R

	# now populate arrays with all the data
	for i in range(1, 50):
		# find deltas, put in temporary variables instead of overall calculation because they are interdependent
		ndS = deltaS(sarray[i - 1], iarray[i - 1], e, p, u, N, B)
		ndv = deltav(varray[i - 1], e, p, u, N)
		ndI = deltaI(iarray[i - 1], sarray[i - 1], B, y, u, k)
		ndR = deltaR(rarray[i - 1], iarray[i - 1], y, u)
		# find overalls, put in temporaries
		nS = newOverall(sarray[i - 1], ndS)
		nv = newOverall(varray[i - 1], ndv)
		nI = newOverall(iarray[i - 1], ndI)
		nR = newOverall(rarray[i - 1], ndR)

		# don't allow populations to go below zero
		# because you can't have negative people...
		# well thay can be nagative, Nick
		if nS <= 0:
			nS = 0
		if nv <= 0:
			nv = 0
		if nI <= 0:
			nI = 0
		if nR <= 0:
			nR = 0
		# prevent any of the sub populations to be larger than overall
		# because that doesn't work either
		if nS >= N:
			nS = N
		if nv >= N:
			nv = N
		if nI >= N:
			nI = N
		if nR >= N:
			nR = N

		# now store temps in arrays for graphing
		sarray[i] = nS
		varray[i] = nv
		iarray[i] = nI
		rarray[i] = nR
		narray[i] = nS + nv + nI + nR

	# only need one x array
	x = np.arange(0, 50, 1)

	# plot arrays, no for loop because that adds performance overhead
	plot(x, sarray)
	plot(x, varray)
	plot(x, iarray)
	plot(x, rarray)
	plot(x, narray)

	# add all the regular graph stuffs
	xlabel('Time (Years)')
	ylabel('Population (Hundreds of millions)')
	legend(['Susceptable', 'Vaccinated', 'Infected', 'Recovered', 'Total'])
	title('Impact of Malaria on the population of Nigeria')
	#axis([0, 50, 0, 300000])
	grid(True)
	axhline(0, color='black', lw=2)
	axvline(0, color='black', lw=2)
	show()
	return

# declerations to avoid dot syntax which introduces a performance overhead
empties = np.empty
stringy = tk.StringVar

# tkinter window to edit constants
def tkwindow():
	# declare window and give it a title
	window = tk.Tk()
	window.title('Options')
	# Variables as strings for display
	variables = ['N', 'B', 'u', 'y', 'e', 'p', 'v', 'I', 'R', 'k']
	descriptors = ['Total Population', 'Force of Infection', 'Death Rate in Overall Population', 'Recovery Rate', 'Vaccine Take, Percentage that are Protected', 'Percentage Vaccinated at Birth', 'Vaccinated Population', 'Infected Population', 'Recovered Population', 'Death Rate from Malaria']
	stringVariables = [stringy(), stringy(), stringy(), stringy(), stringy(), stringy(), stringy(), stringy(), stringy(), stringy()]
	defaults = ['183500000', '0.000000016123288', '0.0016348773841961854', '0.5', '0.8', '0.830076', '0', '100', '0', '0.25']
	
	# loop through lists to produce tkinter widgets with relavent data
	for i in range(0, 10):
		stringVariables[i].set(defaults[i])
		tk.Entry(window, textvariable = stringVariables[i]).grid(row = i, column = 2)
		tk.Label(window, text = variables[i]).grid(row = i, column = 1)
		tk.Label(window, text = descriptors[i]).grid(row = i, column = 0)

	tk.Button(window, text = 'Graph', command = lambda stringVariables=stringVariables: main(stringVariables)).grid(row = i + 1, columnspan = 3)

	window.mainloop()

tkwindow()