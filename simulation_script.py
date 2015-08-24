import Simulator
import PackageGenerator

pg = PackageGenerator.PackageGenerator(10, 'constant')
simulator = Simulator.Simulator(run_time=1000)
simulator.simulate(pg)