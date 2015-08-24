import numpy as np

class Simulator:

	def __init__(self, run_time=100, package_limit=100, 
		         scheduling_type='shortest_queue'):
		self.run_time = run_time
		self.processes = []
		self.resources =[]
		self.package_count = 0
		self.package_limit = package_limit
		self.now = 0
		if (self.run_time < 0):
			raise ValueError('Time only goes forward mate, sorry.')

		self.scheduling_type = scheduling_type
		if (self.scheduling_type not in ['shortest_queue', 'longest_queue', 'random']):
			raise ValueError('Undefined Scheduling Type')

	def simulate(self, init_proc):
		self.processes.append(init_proc)
		while((self.now < self.run_time) and \
			  (self.package_count < self.package_limit)):
			tasklist = [proc.survey() for proc in self.processes]
			self.now += min(tasklist)
			if(self.now > self.run_time):
				break
			current_proc = self.processes[np.argmin(tasklist)]
			current_proc.next_job()
			for proc in self.processes: 
				proc.notify(min(tasklist))

	def add_resource(self, new_server):
		self.resources.append(new_server)
		self.processes.append(new_server)

	def package_manager(self, package):
		available=[]
		for res in self.resources:
			available.append([res, res.available])
		empty_slots = [a[1] for a in available]
		
		if(self.scheduling_type == 'shortest_queue'):
			server_idx = np.argmin(empty_slots)
			available[server_idx][0].arrival(package)
		elif(self.scheduling_type == 'longest_queue'):
			server_idx = np.argmax(empty_slots)
			available[server_idx][0].arrival(package)
		elif(self.scheduling_type == 'random'):
			pass
