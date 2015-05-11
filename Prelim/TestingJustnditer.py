import numpy as np
import time as time

a = np.arange(1000) # 1,000

start = time.time()

for x in np.nditer(a, op_flags = ['readwrite']):
	x = 2 * x

print(format((time.time() - start), '.3'))