import Simulator
import RequestGenerator
import Request
import Resource

RESOURCE_LIM = 5
REQUEST_LIM = 100
RUN_TIME = 10000

simulator = Simulator.Simulator(run_time=RUN_TIME, request_limit=REQUEST_LIM,
	                            scheduling_type='shortest_queue')

for idx in range(1,RESOURCE_LIM+1):
	resource = Resource.Resource(resource_id=idx, simulator=simulator, capacity=5)
	simulator.add_resource(resource)

rg = RequestGenerator.RequestGenerator(lambd=5, process_time=50,
									   simulator=simulator, 
	                                   process_type='constant',
                                       arrival_type='homogeneous')
simulator.simulate(rg)