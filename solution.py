import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time

numSensorNeurons = 9
numMotorNeurons = 8

class SOLUTION:

	def __init__(self, next_id):

		self.weights = 2*numpy.random.rand(numSensorNeurons,numMotorNeurons)-1
		self.myID = next_id

	def Set_ID(self, next_id):
		self.myID = next_id

	# def Evaluate(self, mode_type):
	# 	self.Create_World()
	# 	self.Create_Body()
	# 	self.Create_Brain()
	# 	os.system("python3 simulate.py " + mode_type + " " + str(self.myID) + " &")

	# 	while not os.path.exists("fitness" + str(self.myID) + ".txt"):

	# 		time.sleep(0.01)


	# 	f = open("fitness" + str(self.myID) + ".txt", "r")
	# 	self.fitness = float(f.read())
	# 	f.close()
	
	def Start_Simulation(self,mode_type):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("python3 simulate.py " + mode_type + " " + str(self.myID) + " 2&>1 &")

	def Wait_For_Simulation_To_End(self, delete):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):

			time.sleep(0.01)


		f = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(f.read())
		f.close()
		os.system(delete)

	def Mutate(self):
		random_row = random.randint(0,numSensorNeurons-1)
		random_column = random.randint(0,numMotorNeurons - 1)
		self.weights[random_row,random_column]  =  random.random() * 2 - 1
	def Create_World(self):

		pyrosim.Start_SDF("world.sdf")

		length = 1
		height = 1
		width = 1

		x_1 = 5
		y_1 = 5
		z_1 = 0.5



		pyrosim.Send_Cube(name ="Box", pos=[x_1,y_1,z_1], size=[length, width, height])


		pyrosim.End()


	def Create_Robot(self):
		pass

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		length = 1
		height = 1
		width = 1

		x_1 = 1
		y_1 = 0
		z_1 = 0.5

		pyrosim.Send_Cube(name ="Torso", pos=[0,0,1], size=[length, width, height])


		pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , 
			type = "revolute", position = [-0.5,0,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="LeftLeg", pos=[-0.5,0,0], size=[1.0,0.2,0.2])

		pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , 
			type = "revolute", position = [-1,0,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="LeftLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

		pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , 
			type = "revolute", position = [0.5,0,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="RightLeg", pos=[0.5,0,0], size=[1.0,0.2,0.2])

		pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , 
			type = "revolute", position = [1,0,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="RightLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])


		pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
			type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])

		pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , 
			type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="FrontLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])


		
		pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
			type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="BackLeg", pos=[0,-.5,0], size=[0.2,1,0.2])

		pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , 
			type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name ="BackLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
		
		pyrosim.End()
	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
		pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
		pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
		pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")







		pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")

		pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")

		pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
		pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
		pyrosim.Send_Motor_Neuron( name = 13 , jointName = "FrontLeg_FrontLowerLeg")
		pyrosim.Send_Motor_Neuron( name = 14 , jointName = "BackLeg_BackLowerLeg")
		pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_LeftLowerLeg")
		pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg")






		for currentRow in range(0,numSensorNeurons):
			for currentColumn in range(0,numMotorNeurons):
					pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+numSensorNeurons , weight = self.weights[currentRow][currentColumn])



		# pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 2.0 )
		# pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
		# pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 0.5 )
		# pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )

		pyrosim.End()



	