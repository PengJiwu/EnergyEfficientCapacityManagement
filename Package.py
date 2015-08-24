import numpy as np

class Package:

	def __init__(self, package_id, process_time, arrival_time):
		self.name = 'Package_' + str(package_id)
		self.process_time = process_time
		self.arrival_time = arrival_time
		self.wait_time = 0
		print str(self.arrival_time) + ', ' + self.name + ': I\'m alive!!! '
