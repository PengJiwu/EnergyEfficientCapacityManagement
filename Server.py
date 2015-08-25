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
		self.package_list.append(package)
		print('%3.4f, %s: I arrived to %s. %d slots available.' %(self.simulator.now, package.name, self.name, self.available))
		self.update(1)

	def notify(self, time_step):
		for p in self.package_list:
			p.process_time -= time_step

	def next_job(self):
		timeouts = [p.process_time for p in self.package_list]
		package_idx = np.argmin(timeouts)
		print('%3.4f, %s: I\'m leaving %s. %d slots available.' %(self.simulator.now, self.package_list[package_idx].name, self.name, (self.available+1)))
		del self.package_list[package_idx]
		self.update(-1)

	def update(self, change):
		self.available = self.capacity - len(self.package_list)
		if(len(self.package_list) - change == 0):
			return
		else:
			print 'The expected completions before update:'
			for p in self.package_list:
				print('\t%s:\t%3.3f' % (p.name, p.process_time))

			for p in self.package_list:
				cur_len = len(self.package_list) * 1.0
				prev_len = (len(self.package_list) - change) * 1.0
				new_process_time = p.process_time * (cur_len / prev_len)
				p.process_time = new_process_time

			print 'The expected completions afters update:'
			for p in self.package_list:
				print('\t%s:\t%3.3f' % (p.name, p.process_time))
