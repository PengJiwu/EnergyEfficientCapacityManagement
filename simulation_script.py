import numpy as np
import CapacityManager
import Simulator
import RequestGenerator
import Request
import Resource

RESOURCE_LIM = 5
REQUEST_LIM = 100
RUN_TIME = 10000

simulator = Simulator.Simulator(run_time=RUN_TIME, request_limit=REQUEST_LIM,
	                            scheduling_type='longest_queue')

capacity_manager = CapacityManager.CapacityManager(2, 5, simulator, 5)

rg = RequestGenerator.RequestGenerator(lambd=5, process_time=50, simulator=simulator, 
	                                   process_type='constant', arrival_type='homogeneous')

simulator.simulate()