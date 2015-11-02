import numpy as np
import sys
sys.path.insert(0, './classes/')
import CapacityManager
import Simulator
import RequestGenerator
import Request
import Resource

"""Simulation Parameters--------------------------------------------"""
T_HIGH = 10						# Upper threshold value
T_LOW = 3						# Lower threshold value
LAMBD = 5 						# Arrival rate
RESOURCE_CAP = 5 				# Capacity of each server
REQ_LIM = 100 					# Number of Requests to be served
RUN_TIME = 10000 				# Time limit of the simulation
BOOT_TIME = 10 					# The time it takes for a server to turn on
PROCESS_TIME = 100  			# The duration of a single request
ROUTING = 'longest_queue'		# Routing method. Can be: longest_queue,
								# shortest_queue or random
"""-----------------------------------------------------------------"""

simulator = Simulator.Simulator(RUN_TIME, REQ_LIM, ROUTING)

capacity_manager = CapacityManager.CapacityManager(T_LOW, T_HIGH, simulator, RESOURCE_CAP, BOOT_TIME)

rg = RequestGenerator.RequestGenerator(LAMBD, PROCESS_TIME, simulator, process_type='constant',
									   arrival_type='homogeneous', lambd_bins = None)

simulator.simulate()