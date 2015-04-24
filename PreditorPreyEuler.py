# graph a population of foxes and rabbits in a classic preditor prey senario
# rabbits: dx/dt = 0.8x - 0.04xy
# foxes: dy/dt = -0.3y + 0.006xy

from matplotlib.pylab import *
import numpy as np

def rabbitChange(rabbitsP, foxesP):
	print(0.8*rabbitsP - (0.04 * rabbitsP * foxesP))
	return (0.8*rabbitsP - (0.04 * rabbitsP * foxesP))

def newRabbits(currentRabbits, currentFoxes):
	return (currentRabbits + (rabbitChange(currentRabbits, currentFoxes) * deltaT))

def foxChange(rabbitsP, foxesP):
	return (-0.3*foxesP + (0.006 * rabbitsP * foxesP))

def newFoxes(currentRabbits, currentFoxes):
	return (currentFoxes + (foxChange(currentRabbits, currentFoxes) * deltaT))

foxes = 10
rabbits = 55
t = 0
deltaT= 0.1
rabbity = np.empty(1000)
foxy = np.empty(1000)
x = np.arange(0, 100, deltaT)
for i in range(0, 1000):
	newRab = newRabbits(rabbits, foxes)
	newFox = newFoxes(rabbits, foxes)
	rabbity[i] = newRab
	foxy[i] = newFox
	rabbits = newRab
	foxes = newFox
	t += deltaT
print(rabbity)
plot(x,rabbity)
plot(x,foxy)
axis([0, 100, amin(foxy), amax(rabbity)])
xlabel('t')
ylabel('Foxes and Rabbits')
legend('')
show()