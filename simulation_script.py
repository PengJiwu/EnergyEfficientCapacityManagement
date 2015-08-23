import Simulator
import PackageGenerator

pg = PackageGenerator.PackageGenerator(5, 'constant')
simulator = Simulator.Simulator(run_time=100)
simulator.simulate(pg)