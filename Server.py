import Package
import Simulator
import numpy as np

class Server:

	def __init__(self, server_id, simulator, capacity=5):
		self.name = 'Server_' + str(server_id)
		self.simulator = simulator
		self.capacity = capacity
		self.package_list = []
		self.available = self.capacity - len(self.package_list)

	def survey(self):
		timeouts = [p.process_time for p in self.package_list]
		if timeouts :
			return min(timeouts)
		else:
			return self.simulator.run_time

	def arrival(self, package):
		print self.available
		print str(self.simulator.now) + ', ' + package.name + ': I arrived'
		self.package_list.append(package)
		self.update(1)

	def notify(self, time_step):
		for p in self.package_list:
			p.process_time -= time_step

	def next_job(self):
		timeouts = [p.process_time for p in self.package_list]
		package_idx = np.argmin(timeouts)
		print str(self.simulator.now) + ', ' + self.package_list[package_idx].name + \
		      ': I\'m leaving'
		del self.package_list[package_idx]
		self.update(-1)

	def update(self, change):
		if(len(self.package_list) - change == 0):
			return
		else:
			self.available = self.capacity - len(self.package_list)
			for p in self.package_list:
				p.process_time = p.process_time * (len(self.package_list) / \
					             (len(self.package_list) - change))
