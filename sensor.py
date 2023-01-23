import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class SENSOR:

	def __init__(self, linkName):

		self.linkName = linkName
		self.values = numpy.zeros(1000)

	def Get_Value(self, index):
		self.values[index] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

