import numpy as np
import sys
sys.path.insert(0, './classes/')
import CapacityManager
import Simulator
import RequestGenerator
import Request
import Resource

"""Simulation Parameters--------------------------------------------"""
T_HIGH = 3			# Upper threshold value
T_LOW = 1 			# Lower threshold value
LAMBD = 5 			# Arrival rate
RESOURCE_CAP = 5 	# Capacity of each server
REQUEST_LIM = 100 	# Number of Requests to be served
RUN_TIME = 10000 	# Time limit of the simulation
"""-----------------------------------------------------------------"""

simulator = Simulator.Simulator(run_time=RUN_TIME, request_limit=REQUEST_LIM,
	                            scheduling_type='shortest_queue')

capacity_manager = CapacityManager.CapacityManager(T_LOW, T_HIGH, simulator, RESOURCE_CAP)

rg = RequestGenerator.RequestGenerator(lambd=5, process_time=50, simulator=simulator, 
	                                   process_type='constant', arrival_type='homogeneous')

simulator.simulate()