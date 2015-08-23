import numpy as np

class Simulator:

	def __init__(self, run_time=100):
		self.run_time = run_time
		self.processes = []
		self.now = 0
		if (self.run_time < 0):
			raise ValueError('Time only goes forward mate, sorry.')

	def simulate(self, init_proc):
		self.processes.append(init_proc)
		while(self.now < self.run_time):
			tasklist = [proc.survey() for proc in self.processes]
			self.now += min(tasklist)
			if(self.now > self.run_time):
				break
			self.processes[np.argmin(tasklist)].next_job(self.now)