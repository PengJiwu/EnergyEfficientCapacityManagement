import Package
import numpy as np
from random import expovariate

class PackageGenerator:

	def __init__(self, lambd, process_time, process_type='constant'):
		self.lambd = lambd
		self.package_count = 0
		self.process_time = process_time
		self.upcoming = self.next_arrival()
		self.process_type = process_type if process_type in \
		                    ['constant', 'poisson'] else None
		if(self.process_type is None):
			raise ValueError('Undefined Process Type')

	def generate_package(self, package_id, process_time, dob):
		self.package_count += 1
		return Package.Package(package_id, process_time, dob)

	def next_arrival(self):
		return expovariate(1.0 / self.lambd)

	def survey(self):
		return self.upcoming

	def next_job(self, timestamp):
		self.generate_package(self.package_count,
							  self.next_process_time(), timestamp)

	def next_process_time(self):
		if (self.process_type == 'constant'):
			return self.process_time
		elif (self.process_type == 'poisson'):
			return expovariate(1.0 / self.process_time)