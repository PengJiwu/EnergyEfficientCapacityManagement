import numpy as np
from random import randint

class Simulator:

	def __init__(self, run_time=100, package_limit=100, 
		         scheduling_type='shortest_queue'):
		self.run_time = run_time
		self.processes = []
		self.resources =[]
		self.package_count = 0
		self.package_limit = package_limit
		self.package_queue = []
		self.now = 0
		if (self.run_time < 0):
			raise ValueError('Time only goes forward mate, sorry.')

		self.scheduling_type = scheduling_type
		if (self.scheduling_type not in ['shortest_queue', 'longest_queue', 'random']):
			raise ValueError('Undefined Scheduling Type')

	def simulate(self, init_proc):
		self.processes.append(init_proc)
		while((self.now < self.run_time) and \
			  (self.package_count < self.package_limit)):
			tasklist = [proc.survey() for proc in self.processes]
			time_step = min(tasklist)
			current_proc = self.processes[np.argmin(tasklist)]
			if(time_step == 0): #DEBUG
				break
			self.now += time_step
			if(self.now > self.run_time):
				break

			# Countdown the waiting job's waiting time by time_step
			for proc in self.processes: 
				proc.notify(time_step)
			
			# Activate the first job in line
			current_proc.next_job()

			# Retry allocating queued packages
			if self.package_queue:
				self.package_routing(self.package_queue[0])

	def add_resource(self, new_server):
		self.resources.append(new_server)
		self.processes.append(new_server)

	def package_routing(self, package):
		free_slots = []
		free_servers = []
		for server in self.resources:
			if(server.available > 0):
				free_slots.append(server.available)
				free_servers.append(server)
		free_slots = np.array(free_slots)

		# There is some available capacity
		if free_slots.tolist():	
			if(self.scheduling_type == 'shortest_queue'):
				server_idx = np.argmax(free_slots)
			elif(self.scheduling_type == 'longest_queue'):
				server_idx = np.argmin(free_slots)
			elif(self.scheduling_type == 'random'):
				server_idx = randint(0,(len(free_slots)-1))
			free_servers[server_idx].arrival(package)

			# This package was queued before. Remove it from queue
			if(package in self.package_queue):
				self.package_queue.remove(package)
		else:
			if package not in self.package_queue:
				#else it's already in the queue
				print ('%3.4f, %s: I\'m going to queue' % (self.now, package.name))
				self.package_queue.append(package)