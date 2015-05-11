import numpy as np
import time as time

a = np.arange(100000000) # 1,000,000,000

start = time.time()

for x in range(0,100000000):
	a[x] = a[x] * 2

print(format((time.time() - start), '.3'))