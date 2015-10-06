import numpy as np

class Request:

	def __init__(self, request_id, process_time, generation_time, arrival_time=0):
		self.name = 'Request_' + str(request_id)
		self.process_time = process_time
		self.generation_time = generation_time
		self.arrival_time = arrival_time