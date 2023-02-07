import numpy
import pybullet as p
import pybullet_data
import math
import pyrosim.pyrosim as pyrosim
class SENSOR:

	def __init__(self, linkName):

		self.linkName = linkName
		self.values = numpy.zeros(1000)

	def Get_Value(self, index):

		self.values[index] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

	def Get_Value_CPG(self, index):

		x = 1000

		self.values[index] = math.sin(index * x)



