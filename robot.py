import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK



class ROBOT:

	def __init__(self):

		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain.nndf")



	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self,index):
		# print(self.sensors.values())
		for sensor_type in self.sensors.values():
			sensor_type.Get_Value(index)

	def Prepare_To_Act(self):
		self.motors = {}
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self, index):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[jointName.encode('UTF-8')].Set_Value(self.robotId, desiredAngle)



				# for motor_type in self.motors.values():
		 	# 		motor_type.Set_Value(self.robotId,desiredAngle)
				print(neuronName, jointName);


		# for motor_type in self.motors.values():
		# 	motor_type.Set_Value(self.robotId,desiredAngle)

	def Think(self):
		self.nn.Update()


		self.nn.Print()








