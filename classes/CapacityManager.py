import numpy as np
import Resource

class CapacityManager:

	def __init__(self, t_low, t_high, simulator, res_cap, boot_time, monitor):
		self.simulator = simulator
		self.boot_time = boot_time
		self.res_cap = res_cap
		self.res_cnt = 0
		if(t_low >= t_high):
			raise ValueError('Upper limit is not larger than lower limit')
		self.t_low = t_low
		self.t_high = t_high
		self.monitor = monitor
		self.initialize_capacity()

	def initialize_capacity(self):
		self.simulator.capacity_manager = self
		init_cnt = int((self.t_high - self.t_low) / 2)
		for _ in xrange(init_cnt):
			self.generate_resource()

	def manage_capacity(self, resource_queue):
		idle_idxs = []
		idle_cnt = 0
		
		for resource in resource_queue:
			if(resource.available == resource.capacity):
				idle_idxs.append(resource.available)
				idle_cnt += 1

		if (idle_cnt < self.t_low):
			diff = self.t_low - idle_cnt
			for _ in xrange(diff):
				self.generate_resource()

		elif (idle_cnt > self.t_high):
			diff = idle_cnt - self.t_high
			for i in xrange(diff):
				self.simulator.resources[idle_idxs[i]].shutdown()
				self.simulator.del_resource(idle_idxs[i])

	def generate_resource(self):
		resource = Resource.Resource((self.res_cnt+1), self.simulator,
									 self.boot_time, self.monitor, self.res_cap)
		self.res_cnt += 1
		self.simulator.add_resource(resource)

