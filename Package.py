import numpy as np

class Package:

	def __init__(self, package_id, process_time, generation_time, arrival_time=0):
		self.name = 'Package_' + str(package_id)
		self.process_time = process_time
		self.generation_time = generation_time
		self.arrival_time = arrival_time
