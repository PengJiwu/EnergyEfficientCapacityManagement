import numpy as np
from random import randint

class Simulator:

	def __init__(self, monitor, run_time=100, request_limit=100, 
		         scheduling_type='shortest_queue'):
		self.monitor = monitor			   # monitor for evaluating performance 
		self.processes = []				   # list of parallel processes (threads)
		self.resources =[]				   # list of resources
		self.request_count = 0 			   # number of requests processed
		self.request_limit = request_limit # number of requests to be processed
		self.request_queue = []			   # queue of requests waiting for service
		self.now = 0					   # the time of simulation environment
		self.capacity_manager = None
		if (run_time < 0):
			raise ValueError('Time goes forward mate, enter a positive value.')
		else:
			self.run_time = run_time		   # max. duration of simulation

		if (scheduling_type not in ['shortest_queue', 'longest_queue', 'random']):
			raise ValueError('Undefined scheduling type')
		else:
			self.scheduling_type = scheduling_type # routing method of requests

	def go_on(self):
		# Time is over buddy. Gotta stop
		if self.now >= self.run_time:
			print "Overtime"
			return False
		# Enough requests had been processed
		if self.request_count >= self.request_limit:
			print "Retired"
			return False
		return True

	def simulate(self):
		while(self.go_on()):
			self.capacity_manager.manage_capacity(self.resources)
			tasklist = [proc.survey() for proc in self.processes]
			time_step = min(tasklist)
			current_proc = self.processes[np.argmin(tasklist)]
			self.now += time_step

			# Countdown the waiting job's waiting time by time_step
			for proc in self.processes: 
				proc.notify(time_step)
			
			# Activate the first job in line
			current_proc.next_job()

			# Retry allocating queued requests
			if self.request_queue:
				self.request_routing(self.request_queue[0])

		# Simulation iteration is over.

		self.monitor.finalize(self)

	def add_resource(self, new_resource):
		self.resources.append(new_resource)
		self.processes.append(new_resource)

	def del_resource(self, del_idx):
		resource = self.resources[del_idx]
		self.resources.remove(resource)
		self.processes.remove(resource)

	def request_routing(self, request):
		free_slots = []
		free_resources = []
		for resource in self.resources:
			if((resource.initialized) and (resource.available > 0)):
				free_slots.append(resource.available)
				free_resources.append(resource)
		free_slots = np.array(free_slots)

		# If there is some available capacity
		if free_slots.tolist():	
			if(self.scheduling_type == 'shortest_queue'):
				resource_idx = np.argmax(free_slots)
			elif(self.scheduling_type == 'longest_queue'):
				resource_idx = np.argmin(free_slots)
			elif(self.scheduling_type == 'random'):
				resource_idx = randint(0,(len(free_slots)-1))
			free_resources[resource_idx].arrival(request)

			# This request was queued before. Remove it from queue
			if(request in self.request_queue):
				self.request_queue.remove(request)
		else:
			if request not in self.request_queue:
				#else it's already in the queue
				print ('%3.4f, %s: I\'m going to queue' % (self.now, request.name))
				self.request_queue.append(request)