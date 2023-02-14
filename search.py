import os
#from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
# phc.Show_Best()

# for x in range(0,5):
	# os.system("python3 generate.py")
	# os.system("python3 simulate.py")

