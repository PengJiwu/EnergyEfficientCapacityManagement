import Simulator
import PackageGenerator
import Server

SERVER_LIM = 5
PACKAGE_LIM = 100
RUN_TIME = 10000

simulator = Simulator.Simulator(run_time=RUN_TIME, package_limit=PACKAGE_LIM,
	                            scheduling_type='shortest_queue')

for idx in range(1,SERVER_LIM+1):
	server = Server.Server(server_id=idx, simulator=simulator, capacity=5)
	simulator.add_resource(server)

pg = PackageGenerator.PackageGenerator(lambd=5, process_time=50,
									   simulator=simulator, 
	                                   process_type='constant',
                                       arrival_type='homogeneous')
simulator.simulate(pg)