import Package
import numpy as np

class Server:

	def __init__(self, capacity=5):
		self.capacity = capacity
		self.queue = [None for x in xrange(self.capacity)]
		self.upcoming = []
		self.available = self.queue.count(None)

	def survey(self):
		return min(self.upcoming)