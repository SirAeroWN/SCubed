# graph a population of foxes and rabbits in a classic preditor prey senario
# rabbits: dx/dt = 0.8x - 0.04xy
# foxes: dy/dt = -0.3y + 0.006xy

from matplotlib.pylab import *
import numpy as np
import tkinter as tk

def rabbitChange(aP, bP, rabbitsP, foxesP):
	return (aP*rabbitsP - (bP * rabbitsP * foxesP))

def newRabbits(aP, bP, currentRabbits, currentFoxes):
	return (currentRabbits + (rabbitChange(aP, bP, currentRabbits, currentFoxes) * deltaT))

def foxChange(cP, dP, rabbitsP, foxesP):
	return (-1*cP*foxesP + (dP * rabbitsP * foxesP))

def newFoxes(cP, dP, currentRabbits, currentFoxes):
	return (currentFoxes + (foxChange(cP, dP, currentRabbits, currentFoxes) * deltaT))

def update():
	rabbityData, foxyData = calculateYs(eval(astr.get()), eval(bstr.get()), eval(cstr.get()), eval(dstr.get()), eval(foxesstr.get()), eval(rabbitsstr.get()), deltaT, eval(maxTstr.get()))
	close()
	x = np.arange(0, maxT, deltaT)
	plot(x,rabbityData)
	plot(x,foxyData)
	axis([0, maxT, amin(foxyData), amax(rabbityData)])
	xlabel('t')
	ylabel('Foxes and Rabbits')
	legend('')
	show()
	return

def calculateYs(aP, bP, cP, dP, foxesP, rabbitsP, deltaTP, maxTP):
	foxes = foxesP
	rabbits = rabbitsP
	deltaT= deltaTP
	maxT = maxTP
	rabbity = np.empty(int(maxT/deltaT))
	foxy = np.empty(int(maxT/deltaT))
	for i in range(0, int(maxT/deltaT)):
		newRab = newRabbits(aP, bP, rabbits, foxes)
		newFox = newFoxes(cP, dP, rabbits, foxes)
		rabbity[i] = newRab
		foxy[i] = newFox
		rabbits = newRab
		foxes = newFox
	return rabbity, foxy

# now make a simple tkinter window to adjust displays
root = tk.Tk()

# now make labels
tk.Label(root, text = 'a').grid(row = 1, column = 1)
tk.Label(root, text = 'b').grid(row = 2, column = 1)
tk.Label(root, text = 'c').grid(row = 3, column = 1)
tk.Label(root, text = 'd').grid(row = 4, column = 1)
tk.Label(root, text = 'starting rabbits').grid(row = 5, column = 1)
tk.Label(root, text = 'starting foxes').grid(row = 6, column = 1)
tk.Label(root, text = 'maximum time').grid(row = 7, column = 1)

# now set up text vars for each variable
astr = tk.StringVar()
bstr = tk.StringVar()
cstr = tk.StringVar()
dstr = tk.StringVar()
rabbitsstr = tk.StringVar()
foxesstr = tk.StringVar()
maxTstr = tk.StringVar()

# set them to defaults
astr.set('0.8')
bstr.set('0.04')
cstr.set('0.3')
dstr.set('0.006')
rabbitsstr.set('55')
foxesstr.set('100')
maxTstr.set('100')

# now make all the entryboxes
tk.Entry(root, textvariable = astr).grid(row = 1, column = 2)
tk.Entry(root, textvariable = bstr).grid(row = 2, column = 2)
tk.Entry(root, textvariable = cstr).grid(row = 3, column = 2)
tk.Entry(root, textvariable = dstr).grid(row = 4, column = 2)
tk.Entry(root, textvariable = rabbitsstr).grid(row = 5, column = 2)
tk.Entry(root, textvariable = foxesstr).grid(row = 6, column = 2)
tk.Entry(root, textvariable = maxTstr).grid(row = 7, column = 2)

# make a button to update the graph
tk.Button(root, text = 'graph', command = update).grid(row = 8, columnspan = 2)

# foxes = 10
# rabbits = 55
deltaT = 0.01
maxT = 100
# rabbity, foxy = calculateYs(eval(astr.get()), eval(bstr.get()), eval(cstr.get()), eval(dstr.get()), eval(foxesstr.get()), eval(rabbitsstr.get()), deltaT, eval(maxTstr.get()))
# x = np.arange(0, maxT, deltaT)
# plot(x,rabbity)
# plot(x,foxy)
# axis([0, maxT, amin(foxy), amax(rabbity)])
# xlabel('t')
# ylabel('Foxes and Rabbits')
# legend('')
# show()

root.mainloop()