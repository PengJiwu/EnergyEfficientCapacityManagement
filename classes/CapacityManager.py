import numpy as np
import Resource

class CapacityManager:

	def __init__(self, L, U, simulator, res_cap, boot_time, monitor):
		self.simulator = simulator
		self.boot_time = boot_time
		self.res_cap = res_cap
		self.res_cnt = 0
		if(L >= U):
			raise ValueError('Upper limit is not larger than lower limit')
		self.L = L
		self.U = U
		self.monitor = monitor
		self.initialize_capacity()

	def initialize_capacity(self):
		self.simulator.capacity_manager = self
		init_cnt = int((self.U - self.L) / 2)
		for _ in range(init_cnt):
			self.generate_resource()
		for r in self.simulator.resources:
			r.initialized = True

	def manage_capacity(self, resource_queue):
		idle_idxs = []
		idle_cnt = 0
		total_cap = 0
		
		for resource in resource_queue:
			total_cap += resource.available
			if(resource.available == resource.capacity):
				idle_idxs.append(resource.available)
				idle_cnt += 1

		if (total_cap < self.L):
			diff = int((self.L - idle_cnt) / self.res_cap)
			for _ in range(diff):
				self.generate_resource()

		elif (total_cap > self.U):
			diff = int((idle_cnt - self.U) / self.res_cap)
			for i in range(diff):
				self.simulator.resources[idle_idxs[i]].shutdown()
				self.simulator.del_resource(idle_idxs[i])

	def generate_resource(self):
		resource = Resource.Resource((self.res_cnt+1), self.simulator,
									 self.boot_time, self.monitor, self.res_cap)
		self.res_cnt += 1
		self.simulator.add_resource(resource)

