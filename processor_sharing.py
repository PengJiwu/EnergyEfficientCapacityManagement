import simpy
from random import expovariate

def generate(lambd):
	# First package arrives
	Package(env=env, name="Package1")

	# Interarrival Poisson Process
	t = expovariate(1.0 / lambd)
	yield env.timeout(t)

	# Second package arrives
	Package(env=env, name="Package2")

def update_resources(change):
	# No need to update. This is the first arrival to an idle server
	if(res.count - change == 0):
		return
	else:
		print 'Processor Sharing!'
		print env._queue
		for idx, timeout in enumerate(env._queue):
			print timeout
			print timeout[3].callbacks
			if(type(timeout[3].callbacks[0].im_self) is not simpy.Process):
				continue
			timeout_source = timeout[3].callbacks[0].im_self._desc()
			timeout_source = timeout_source[timeout_source.index("(") + \
			                                1:timeout_source.rindex(")")]
			if(timeout_source == 'get_service'):
				remaining = timeout[0] - env.now()
				new_delay = remaining * (res.count/(res.count-change))
				timeout[3]._delay = new_delay
				env._queue[idx] = (new_delay, timeout[1], timeout[2], timeout[3])
		print env._queue

class Package(object):
	def __init__(self, env, name):
		self.env = env
		self.name = name
		env.process(self.get_service())

	def get_service(self):
		# Package arrival and resource request
		arrive_time = env.now
		request = res.request()
		print("%3.2f\t: %s arrived at %3.2f" % (env.now, self.name, arrive_time))
		yield request

		# Request is accepted, service starts
		update_resources(1)
		wait_time = env.now - arrive_time
		print("%3.2f\t: %s Waited %3.2f" % (env.now, self.name, wait_time))
		yield env.timeout(process_time)

		# Service is completed
		update_resources(-1)
		print("%3.2f\t: %s done" % (env.now, self.name))

# Simulation Parameters
process_time = 20
simulate_time = 1000
lambd = 5

# Simulation Run
env = simpy.Environment()
res = simpy.Resource(env, capacity=2)
env.process(generate(lambd))
env.run(until=simulate_time)