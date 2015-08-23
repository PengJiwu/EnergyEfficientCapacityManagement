import numpy as np

class Package:

	def __init__(self, package_id, process_time, dob):
		self.name = 'Package_' + str(package_id)
		self.process_time = process_time
		self.dob = dob
		print str(self.dob) + ', ' + self.name + ': I\'m alive!!! '  
