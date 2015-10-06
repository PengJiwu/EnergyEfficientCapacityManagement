import numpy as np

import Simulator
import RequestGenerator
import Request
import Resource

RESOURCE_LIM = 5
REQUEST_LIM = 100
RUN_TIME = 10000

# Loading the nonhomogeneous poisson process lambda(t) values. 1st column
# represents the endpoints of the histogram and the vals are corresponding
# histogram values.
lambd = np.loadtxt('./nhpp_data/sinusoid.txt')
lambd_bins = lambd[:,0]
lambd_vals = lambd[:,1]

simulator = Simulator.Simulator(run_time=RUN_TIME, request_limit=REQUEST_LIM,
	                            scheduling_type='shortest_queue')

for idx in range(1,RESOURCE_LIM+1):
	resource = Resource.Resource(resource_id=idx, simulator=simulator, capacity=5)
	simulator.add_resource(resource)

rg = RequestGenerator.RequestGenerator(lambd=lambd_vals, process_time=50, simulator=simulator, 
	                                   process_type='constant', arrival_type='nonhomogeneous',
	                                   lambd_bins=lambd_bins)
simulator.simulate(rg)