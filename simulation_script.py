import Simulator
import PackageGenerator
import Server

simulator = Simulator.Simulator(run_time=1000, package_limit=20,
	                            scheduling_type='shortest_queue')

server = Server.Server(server_id=1, simulator=simulator, capacity=5)
simulator.add_resource(server)

pg = PackageGenerator.PackageGenerator(lambd=5, process_time=20,
									   simulator=simulator, 
	                                   process_type='constant',
                                       arrival_type='homogeneous')
simulator.simulate(pg)