# dS/dt=((1-e*p)*u*N)-(B*(dI/dt)*(dS/dt))-(u*(dS/dt))
# dv/dt=e*p*u*N-u*(dv/dt)
# dI/dt=B*(dI/dt)*(dS/dt)-y*(dI/dt)-u*(dI/dt)
# dR/dt=y*(dI/dt)-u*(dR/dt)

def deltaS(dSp, dIp):
	return ((((1 - e) * p) * u * N) - (B * dIp * dSp) - (u * dSp))

def deltav(dvs):
	return (e * p * u * N - u * dvs)

def deltaI(dIp, dSp):
	return (B * dIp * dSp - y * dIp - u * dIp)

def deltaR(dRp, dIp):
	return (y*dIp-u*dRp)

def newOverall(previous, deltaVal):
	return (previous + deltaVal)

N = 183500000
B = 0.016123288
u = (300000 / 183500000)
y = 3.227642
e = 1
p = 0.830076
dS = 182000999
dv = 0
dI = 22
dR = 0
S = 0
v = 0
I = 0
R = 0

print('s:', deltaS(dS, dI), '\nv:', deltav(dv), '\nI:', deltaI(dI, dS), '\nR:', deltaR(dR, dI))

for i in range(1, 51):
	ndS = deltaS(dS, dI)
	ndv = deltav(dv)
	ndI = deltaI(dI, dS)
	ndR = deltaR(dR, dI)
	S = newOverall(S, ndS)
	v = newOverall(v, ndv)
	I = newOverall(I, ndI)
	R = newOverall(R, ndR)
	dS = ndS
	dv = ndv
	dI = ndI
	dR = ndR
	print('\n', i,'\n\ts:', dS, '\n\tv:', dv, '\n\tI:', dI, '\n\tR:', dR)