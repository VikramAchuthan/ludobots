import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim


class MOTOR:

	def __init__(self, jointName):

		self.jointName = jointName
		self.Prepare_To_Act()
	def Prepare_To_Act(self):


		self.amplitude = (numpy.pi)/4
		self.frequency= 2
		print(self.jointName)
		if self.jointName == b'Torso_FrontLeg':
			self.frequency = 1
		self.phaseOffset = (numpy.pi)/4
		
		self.motorValues = numpy.linspace(0, 2 * numpy.pi, 1000)
		for x in range(0,1000):
			self.motorValues[x] = self.amplitude * numpy.sin(self.frequency * self.motorValues[x] + self.phaseOffset)
		
		# targetAngles_FrontLeg = numpy.linspace(0, 2 * numpy.pi, 1000)
		# for x in range(0,1000):
			# 	targetAngles_FrontLeg[x] = amplitude_FrontLeg * numpy.sin(frequency_FrontLeg * targetAngles_FrontLeg[x] + phaseOffset_FrontLeg)
	def Set_Value(self, robot, desiredAngle):
		pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = 1)
