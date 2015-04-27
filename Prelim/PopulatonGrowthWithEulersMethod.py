# approximate dp/dt = 3p(1-p) with euler's method
# eq: dy/dx = 3y(1-y)

from matplotlib.pylab import *
import numpy as np

def popEQ(y):
	return ((3 * y) * (1 - y))

def getNewY(Yn):
	return (Yn + popEQ(Yn) * deltaX)

Y = 0.1
X = 0
deltaX = 0.03
y = np.empty(100)
x = np.arange(0, 3, deltaX)
for i in range(0, 100):
	temp = getNewY(Y)
	y[i] = temp
	Y = temp
	X += deltaX
plot(x,y)
xlabel('t')
ylabel('p')
legend('dp/dt = 3p(1-p)')
show()