import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

import numpy
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")


pyrosim.Prepare_To_Simulate(robotId)

frontLegSensorValues = mumpy.zeros(10000)
for x in range(0,1000):
	p.stepSimulation()
	frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	print(frontLegTouch)
	time.sleep(1/30)
p.disconnect()

