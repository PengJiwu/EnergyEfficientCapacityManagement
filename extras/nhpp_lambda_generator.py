import numpy as np

"""--------------------------------------------------------------------
This is an example script to extract time dependent lambda from actual
data.

LIMITATION: Here we are modelling a Non-staionary Poisson Process,
which implies that requests must arrive one-at-a-time. Multiple
requests can't arrive at the same time. This is a commonly used
approach, but be aware of this limitation, since it might be
problematic depending on your task.
--------------------------------------------------------------------"""

INTERVAL_LEN = 50
LAMBDA_LEN = 1600

lambd = [0 for _ in xrange(LAMBDA_LEN)]

for n, _ in enumerate(lambd):
	lambd[n] = 400 * (np.sin(n / (800/(2*np.pi))) + 1)

# pl.plot(lambd)
# pl.show()

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

with open('sine_lambda.txt', 'w') as f:
	for bn, val in zip(avg_bins, avg_vals):
		f.write(str(bn) + '\t' + str(val) + '\n')
