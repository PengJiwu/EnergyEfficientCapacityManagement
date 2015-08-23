The Python code in this repository is modelling a data center's capacity
management algorithms. We are applying a hysteresis-like approach for
increasing energy efficieny, while keeping the center's performance above a
certain level.

~~This package extensively uses SimPy Discrete Event Simulation library.~~

*Update @ 23.01.2015:* Apparently SimPy doesn't support Processor Sharing models
and its architecture doesn't allow us to do it by ourselves cleanly either.
Hence, we decided not to use SimPy and write our own simulator! 

For the curious readers, SimPy's problem for us was the fact that, it expected
the duration of service times within a server beforehand. Then, these
values would be stored in the environment of the simulation globally. With
such an assumption (service times being deterministic), there was no clean
and orthodox way to model processor sharing, except for time-slicing.
which is like the exact opposite of elegance.

So far, we can keep track of time and randomly generate packages. The designed
backbone is completed and what's left is to introduce the servers and let it
evolve!