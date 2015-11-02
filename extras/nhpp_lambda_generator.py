import numpy as np
import matplotlib.pyplot as pl
from random import randint

"""--------------------------------------------------------------------
This is an example script to extract time dependent lambda from actual
data.

LIMITATION: Here we are modelling a Non-staionary Poisson Process,
which implies that requests must arrive one-at-a-time. Multiple
requests can't arrive at the same time. This is a commonly used
approach, but be aware of this limitation.
--------------------------------------------------------------------"""
INTERVAL_LEN = 50
LAMBDA_LEN = 5000

# Generation of Quickly Varying Trace
lambd = np.zeros(LAMBDA_LEN)

for n, _ in enumerate(lambd):
	lambd[n] = 295 * ((np.sin(n / (16000/(2*np.pi))) + 1) + 0.7 * np.sin(n / (750/(2*np.pi))))


avg_vals = []
avg_bins = []

for i in xrange((LAMBDA_LEN/INTERVAL_LEN) + 1):
	if not i:
		cur_lim = i * INTERVAL_LEN
	else:
		prev_lim = cur_lim
		cur_lim = i * INTERVAL_LEN
		avg = 0
		for j in xrange(prev_lim, cur_lim):
			avg += (lambd[j] / (cur_lim - prev_lim))
		avg_bins.append(cur_lim)
		avg_vals.append(avg)

pl.stem(avg_bins, avg_vals)
pl.show()

with open('./quickly_varying.txt', 'w') as f:
	for bn, val in zip(avg_bins, avg_vals):
		f.write(str(bn) + '\t' + str(val) + '\n')