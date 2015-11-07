import numpy as np
import sys
sys.path.insert(0, './classes/')
import CapacityManager
import Simulator
import RequestGenerator
import Request
import Resource
import Monitor

"""Simulation Parameters--------------------------------------------"""
T_HIGH = 80						# Upper threshold value
T_LOW = 50						# Lower threshold value
#LAMBD = 5 						# Arrival rate
RESOURCE_CAP = 5 				# Capacity of each server
REQ_LIM = 100000				# Number of Requests to be served
RUN_TIME = 5000 				# Time limit of the simulation
BOOT_TIME = 3 					# The time it takes for a server to turn on
PROCESS_TIME = 10 	  			# The duration of a single request
ROUTING = 'longest_queue'		# Routing method. Can be: longest_queue,
								# shortest_queue or random
BOOT_POWER = 100				# Rate of consumption for a booting server
RUN_POWER = 100					# Rate of consumption for a running server
"""-----------------------------------------------------------------"""

lambd = np.loadtxt('./extras/traces/stock_trend.txt')
lambd_bins = lambd[:,0]
lambd_vals = lambd[:,1]

monitor = Monitor.Monitor((BOOT_POWER * BOOT_TIME), RUN_POWER)

simulator = Simulator.Simulator(monitor, RUN_TIME, REQ_LIM, ROUTING)

capacity_manager = CapacityManager.CapacityManager(T_LOW, T_HIGH, simulator, RESOURCE_CAP, BOOT_TIME, monitor)

rg = RequestGenerator.RequestGenerator(lambd_vals, PROCESS_TIME, simulator, monitor, process_type='constant',
									   arrival_type='nonhomogeneous', lambd_bins = lambd_bins)

simulator.simulate()