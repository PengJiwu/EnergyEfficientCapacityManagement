import Package
import Simulator
import numpy as np
from random import expovariate

class PackageGenerator:

	def __init__(self, lambd, process_time, simulator, 
				 process_type='constant', arrival_type='homogeneous'):
		self.lambd = lambd
		self.lambd_idx = 0
		self.package_count = 0
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

	def generate_package(self):
		process_time = self.next_process_time()
		timestamp = self.simulator.now
		self.simulator.package_count += 1
		self.upcoming = self.next_arrival()
		new_package = Package.Package(self.simulator.package_count,
		                              process_time, timestamp)
		self.simulator.package_manager(new_package)

	def next_arrival(self):
		if(self.arrival_type == 'homogeneous'):
			return expovariate(1.0 / self.lambd)
		elif(self.arrival_type == 'nonhomogeneous'):
			self.lambd_idx += 1
			return expovariate(1.0 / self.lambd[(self.lambd.idx) - 1])

	def survey(self):
		return self.upcoming

	def next_job(self):
		self.generate_package()

	def next_process_time(self):
		if (self.process_type == 'constant'):
			return self.process_time
		elif (self.process_type == 'poisson'):
			return expovariate(1.0 / self.process_time)

	def notify(self, time_step):
		self.upcoming -= time_step