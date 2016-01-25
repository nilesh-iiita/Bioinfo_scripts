#!/usr/bin/python
import numpy as ny
def summary(arr):
	import numpy as ny
	import matplotlib.pyplot as plt
	max_val = ny.max(arr)
	min_val = ny.min(arr)
	mean_val  = ny.mean(arr)
	non_zero = ny.nonzero(arr)
	mu, sigma = ny.mean(arr),ny.std(arr)
	count, bins, ignored = plt.hist(arr, 10, normed=True,color='b')
	plt.plot(bins, 1/(sigma * ny.sqrt(2 * ny.pi)) * ny.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
	plt.show()	
