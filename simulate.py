import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

import numpy
import time
import random

amplitude_BackLeg = (numpy.pi)/4
frequency_BackLeg = 1
phaseOffset_BackLeg = (numpy.pi)/4


amplitude_FrontLeg = (numpy.pi)/4
frequency_FrontLeg = 5
phaseOffset_FrontLeg = (numpy.pi)/4

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")


pyrosim.Prepare_To_Simulate(robotId)

frontLegSensorValues = numpy.zeros(1000)
backLegSensorValues = numpy.zeros(1000)

targetAngles_BackLeg = numpy.linspace(0, 2 * numpy.pi, 1000)
for x in range(0,1000):
	targetAngles_BackLeg[x] = amplitude_BackLeg * numpy.sin(frequency_BackLeg * targetAngles_BackLeg[x] + phaseOffset_BackLeg)
numpy.save("data/targetAngles_BackLeg.npy", targetAngles_BackLeg)


targetAngles_FrontLeg = numpy.linspace(0, 2 * numpy.pi, 1000)
for x in range(0,1000):
	targetAngles_FrontLeg[x] = amplitude_FrontLeg * numpy.sin(frequency_FrontLeg * targetAngles_FrontLeg[x] + phaseOffset_FrontLeg)
numpy.save("data/targetAngles_FrontLeg.npy", targetAngles_FrontLeg)


for x in range(0,1000):
	p.stepSimulation()
	frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_BackLeg[x], maxForce = 100)
	pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition =targetAngles_FrontLeg[x], maxForce = 100)


	time.sleep(1/240)

numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)

p.disconnect()

