from simulation import SIMULATION
import sys

# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import constants as c

# import numpy
# import time
# import random

directOrGUI =  sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()

















# numpy.save("data/targetAngles_BackLeg.npy", targetAngles_BackLeg)

# numpy.save("data/targetAngles_FrontLeg.npy", targetAngles_FrontLeg)



# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)



