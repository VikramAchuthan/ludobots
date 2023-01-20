import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
import pyrosim.pyrosim as pyrosim

import time




class SIMULATION:
	def __init__(self):
		

		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())

		# #self.robotId = p.loadURDF("body.urdf")
		p.setGravity(0,0,-9.8)
		#pyrosim.Prepare_To_Simulate(9)


		self.world = WORLD()
		self.robot = ROBOT()
	def Run(self):
		for x in range(0,1000):
			p.stepSimulation()
			self.robot.Sense(x)
			self.robot.Act(x)

			# frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
			# backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
			# pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_BackLeg[x], maxForce = 100)
			# pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition =targetAngles_FrontLeg[x], maxForce = 100)


			time.sleep(1/240)

	def __del__(self):
		p.disconnect()
		