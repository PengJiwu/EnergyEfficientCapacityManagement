import Request
import Simulator
import numpy as np
from random import expovariate

class RequestGenerator:

	def __init__(self, lambd, process_time, simulator, monitor, 
				 process_type='constant', arrival_type='homogeneous',
				 lambd_bins=None):
		self.name = 'RequestGenerator'
		self.lambd = lambd
		self.request_count = 0
		self.process_time = process_time
		self.simulator = simulator
		self.monitor = monitor
		self.passivate = False

		self.simulator.processes.append(self)
		
		if(process_type not in ['constant', 'poisson']):
			raise ValueError('Undefined Process Type')
		self.process_type = process_type

		
		if(arrival_type not in ['homogeneous', 'nonhomogeneous']):
			raise ValueError('Undefined Arrival Type')
		self.arrival_type = arrival_type

		if(self.arrival_type == 'nonhomogeneous'):
			if(lambd_bins is None):
				raise ValueError('Endpoints of Nonhomogeneous Poisson \
								  Arrivals are Unknown') 
			self.lambd_bins = lambd_bins

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
		if(self.passivate):
			return self.simulator.run_time + 1
		else:
			if(self.arrival_type == 'homogeneous'):
				return expovariate(1.0 / self.lambd) 
			elif(self.arrival_type == 'nonhomogeneous'):
				for idx, bn in enumerate(self.lambd_bins):
					if(self.simulator.now < bn):
						break
				# We are now in (idx)^th interval and we choose lambd
				# accordingly. 
				res = 1.0 / expovariate(1.0 / self.lambd[idx])
				# If the expected arrival falls into the next interval,
				# we re-calculate the arrival based on the next lambda.
				while(1):
					if((res + self.simulator.now) > bn):
						if(idx < len(self.lambd_bins) - 1):
							idx += 1
							bn = self.lambd_bins[idx]
							cur_lambd = self.lambd[(idx)]
							res = (bn - self.lambd_bins[idx-1]) + 1.0 / expovariate(1.0 / cur_lambd)
						else:
							self.passivate = True
							return self.simulator.run_time + 1
					else:
						break

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