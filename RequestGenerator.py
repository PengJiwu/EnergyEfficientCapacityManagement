import Request
import Simulator
import numpy as np
from random import expovariate

class RequestGenerator:

	def __init__(self, lambd, process_time, simulator, 
				 process_type='constant', arrival_type='homogeneous'):
		self.name = 'RequestGenerator'
		self.lambd = lambd
		self.lambd_idx = 0
		self.request_count = 0
		self.process_time = process_time
		self.simulator = simulator
		self.process_type = process_type if process_type in \
		                    ['constant', 'poisson'] else None
		if(self.process_type is None):
			raise ValueError('Undefined Process Type')

		self.arrival_type = arrival_type if arrival_type in \
		                    ['homogeneous', 'nonhomogeneous'] else None
		if(self.arrival_type is None):
			raise ValueError('Undefined Arrival Type')

		self.upcoming = self.next_arrival()

	def generate_request(self):
		process_time = self.next_process_time()
		timestamp = self.simulator.now
		self.request_count += 1
		self.upcoming = self.next_arrival()
		new_request = Request.Request(self.request_count,
		                              process_time, timestamp)
		self.simulator.request_routing(new_request)

	def next_arrival(self):
		if(self.arrival_type == 'homogeneous'):
			return expovariate(1.0 / self.lambd) 
		elif(self.arrival_type == 'nonhomogeneous'):
			res = expovariate(1.0 / self.lambd[(self.lambd_idx)])
			self.lambd_idx += 1
			return res

	def survey(self):
		return self.upcoming

	def next_job(self):
		self.generate_request()

	def next_process_time(self):
		if (self.process_type == 'constant'):
			return self.process_time
		elif (self.process_type == 'poisson'):
			return expovariate(1.0 / self.process_time)

	def notify(self, time_step):
		self.upcoming -= time_step