import time
import numpy as np

def timing(f, n, a):
	print(f.__name__, end = ' ')
	r = range(n)
	t1 = time.clock()
	for i in r:
		f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a); f(a)
	t2 = time.clock()
	print(round(t2-t1, 3))
	return

def f1(num):
	a = np.arange(num) # 1,000

	for x in np.nditer(a, op_flags = ['readwrite']):
		x = 2 * x
	return

def f2(num):
	a = np.arange(num) # 1,000,000,000

	for x in range(0, num):
		a[x] = a[x] * 2
	return

timing(f1, 10, 1000)
timing(f2, 10, 1000)