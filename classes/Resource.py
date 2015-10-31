import Request
import Simulator
import numpy as np

class Resource:

	def __init__(self, resource_id, simulator, capacity=5):
		self.name = 'Resource_' + str(resource_id)
		self.simulator = simulator
		self.capacity = capacity
		self.request_list = []
		self.available = self.capacity - len(self.request_list)

	def survey(self):
		timeouts = [r.process_time for r in self.request_list]
		if timeouts :
			return min(timeouts)
		else:
			return self.simulator.run_time

	def arrival(self, request):
		self.request_list.append(request)
		request.arrival_time = self.simulator.now
		self.update(1)
		#print('%3.4f, %s: I arrived to %s. %d slots available.' %(self.simulator.now, request.name, self.name, self.available))

	def notify(self, time_step):
		for r in self.request_list:
			r.process_time -= time_step

	def next_job(self):
		timeouts = [r.process_time for r in self.request_list]
		request_idx = np.argmin(timeouts)
		#print('%3.4f, %s: I\'m leaving %s. %d slots available.' %(self.simulator.now, self.request_list[request_idx].name, self.name, (self.available+1)))
		self.simulator.request_count += 1
		del self.request_list[request_idx]
		self.update(-1)

	def update(self, change):
		self.available = self.capacity - len(self.request_list)
		if(len(self.request_list) - change == 0):
			return
		else:	
			for r in self.request_list:
				cur_len = len(self.request_list) * 1.0
				prev_len = (len(self.request_list) - change) * 1.0
				new_process_time = r.process_time * (cur_len / prev_len)
				r.process_time = new_process_time