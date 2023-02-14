import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time

numSensorNeurons = random.randint(3,6)
numMotorNeurons = 3
class SOLUTION:

	def __init__(self, next_id):

		self.weights = 2*numpy.random.rand(numSensorNeurons,numMotorNeurons)-1
		self.myID = next_id
		self.links_with_sensors = {}

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
		os.system("python3 simulate.py " + mode_type + " " + str(self.myID) + " &") #2&>1

	def Wait_For_Simulation_To_End(self, delete):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):

			time.sleep(0.001)


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



		pyrosim.Send_Cube(name ="Box", pos=[x_1,y_1,z_1], size=[length, width, height],color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')


		pyrosim.End()


	def Create_Robot(self):
		pass

	def Create_Body(self):
		#pyrosim.Start_URDF("body.urdf")
		# length = .5
		# height = .5
		# width = .5

		# x_1 = 1
		# y_1 = 0
		# z_1 = 0.5

		# pyrosim.Send_Cube(name ="Head", pos=[0,0,1], size=[length, width, height])
		# pyrosim.Send_Joint( name = "Head_Neck" , parent= "Head" , child = "Neck" , type = "revolute", 
		# 	position = [0.25,0,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="Neck", pos=[0.25,0,0], size=[length*4, width/2, height])
		# pyrosim.Send_Joint( name = "Neck_Body" , parent= "Neck" , child = "Body" , type = "revolute", 
		#  	position = [.25*4,0,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="Body", pos=[.25,0,0], size=[length, width, height])
		# pyrosim.Send_Joint( name = "Body_Tail" , parent= "Body" , child = "Tail" , type = "revolute", 
		#  	position = [.25,0,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="Tail", pos=[.25,0,0], size=[length, width, height])

		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="Head", pos=[0, 0, 0], size=[1, .1, .1], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
		pyrosim.Send_Joint(name="Head_Neck", parent="Head",child="Neck", type="revolute", position=[-0.5, 0, 0])
		pyrosim.Send_Cube(name="Neck", pos=[0.25, 0, 0], size=[.25, .25, .25], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
		pyrosim.Send_Joint(name="Head_Tail", parent="Head", child="Tail", type="revolute", position=[0.5, 0, 0])
		pyrosim.Send_Cube(name="Tail", pos=[0.5, 0, 0], size=[1, .1, .1], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')

		pyrosim.Send_Joint(name="Tail_Tail1", parent="Tail", child="Tail1", type="revolute", position=[0.5, 0, 0])
		pyrosim.Send_Cube(name="Tail1", pos=[0.5, 0, 0], size=[1, .5, .1], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')
		count = 3
		x = 1
		print("random sensors: ",numSensorNeurons)
		while count < numSensorNeurons:
			print("x: ",x)
			green = random.randint(0,1)
			print(green)
			if(green):
				count+=1
				self.links_with_sensors[x+1] = "Tail" + str(x+1) 
				pyrosim.Send_Joint(name="Tail" + str(x) + "_" + "Tail" + str(x+1), parent="Tail" + str(x), child="Tail" + str(x+1), type="revolute", position=[0.5, 0, 0])
				pyrosim.Send_Cube(name="Tail"+str(x+1), pos=[0.5, 0, 0], size=[1, random.random(), random.random()*1.25], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
			else:
				pyrosim.Send_Joint(name="Tail" + str(x) + "_" + "Tail" + str(x+1), parent="Tail" + str(x), child="Tail" + str(x+1), type="revolute", position=[0.5, 0, 0])
				pyrosim.Send_Cube(name="Tail"+str(x+1), pos=[0.5, 0, 0], size=[1, random.random(), random.random()*1.25], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			x+=1
		while x < numMotorNeurons:
			pyrosim.Send_Joint(name="Tail" + str(x) + "_" + "Tail" + str(x+1), parent="Tail" + str(x), child="Tail" + str(x+1), type="revolute", position=[0.5, 0, 0])
			pyrosim.Send_Cube(name="Tail"+str(x+1), pos=[0.5, 0, 0], size=[1, random.random(), random.random()*1.25], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			x+=1
		
		pyrosim.End()





		# pyrosim.Send_Cube(name ="Torso", pos=[0,0,1], size=[length, width, height])

		# pyrosim.Send_Joint( name = "Torso_Shoulders" , parent= "Torso" , child = "Shoulders" , 
		# 	type = "revolute", position = [0,0,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="Shoulders", pos=[0,0,.5], size=[0.5,0.5,3])

  #   	# ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#

		# pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , 
		# 	type = "revolute", position = [-0.5,-0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="LeftLeg", pos=[-0.5,0,0], size=[1.0,0.2,0.2])
		
		# pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , 
		# 	type = "revolute", position = [-1,0,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="LeftLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

  #   	# ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#

		# pyrosim.Send_Joint( name = "Torso_LeftCornerLeg" , parent= "Torso" , child = "LeftCornerLeg" , 
		# 	type = "revolute", position = [-0.5,0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="LeftCornerLeg", pos=[-0.5,0,0], size=[1.0,0.2,0.2])

		# pyrosim.Send_Joint( name = "LeftCornerLeg_LeftCornerLowerLeg" , parent= "LeftCornerLeg" , child = "LeftCornerLowerLeg" , 
		# 	type = "revolute", position = [-1,0,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="LeftCornerLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

  #   	# ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#


		# pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , 
		# 	type = "revolute", position = [0.5,-0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="RightLeg", pos=[0.5,0,0], size=[1.0,0.2,0.2])

		# pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , 
		# 	type = "revolute", position = [1,0,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="RightLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

  #   	# ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#


		# pyrosim.Send_Joint( name = "Torso_RightCornerLeg" , parent= "Torso" , child = "RightCornerLeg" , 
		# 	type = "revolute", position = [0.5,0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="RightCornerLeg", pos=[0.5,0,0], size=[1.0,0.2,0.2])

		# pyrosim.Send_Joint( name = "RightCornerLeg_RightCornerLowerLeg" , parent= "RightCornerLeg" , child = "RightCornerLowerLeg" , 
		# 	type = "revolute", position = [1,0,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="RightCornerLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

		# # ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#


		# pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
		# 	type = "revolute", position = [0.5,0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])

		# pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , 
		# 	type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="FrontLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

  #   	# ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#

		# pyrosim.Send_Joint( name = "Torso_FrontCornerLeg" , parent= "Torso" , child = "FrontCornerLeg" , 
		# 	type = "revolute", position = [-0.5,0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="FrontCornerLeg", pos=[0,0.5,0], size=[0.2,1,0.2])

		# pyrosim.Send_Joint( name = "FrontCornerLeg_FrontCornerLowerLeg" , parent= "FrontCornerLeg" , child = "FrontCornerLowerLeg" , 
		# 	type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="FrontCornerLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

		# # ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#

		# pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
		# 	type = "revolute", position = [0.5,-.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="BackLeg", pos=[0,-.5,0], size=[0.2,1,0.2])

		# pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , 
		# 	type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="BackLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
		
		# # ~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#


		# pyrosim.Send_Joint( name = "Torso_BackCornerLeg" , parent= "Torso" , child = "BackCornerLeg" , 
		# 	type = "revolute", position = [-0.5,-0.5,1], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="BackCornerLeg", pos=[0,-0.5,0], size=[0.2,1,0.2])

		# pyrosim.Send_Joint( name = "BackCornerLeg_BackCornerLowerLeg" , parent= "BackCornerLeg" , child = "BackCornerLowerLeg" , 
		# 	type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name ="BackCornerLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])


	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Head")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Neck")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Tail")
		count = 3
		for key in self.links_with_sensors.keys():
		 	pyrosim.Send_Sensor_Neuron(name = count , linkName = "Tail" + str(key))
		 	count+=1
		print(self.links_with_sensors)
		print("count:", count)




		pyrosim.Send_Motor_Neuron( name = count , jointName = "Head_Neck")
		pyrosim.Send_Motor_Neuron( name = count+1 , jointName = "Head_Tail")
		pyrosim.Send_Motor_Neuron( name = count+2 , jointName = "Tail_Tail1")


		count+=1
		count+=1
		count+=1
		# for y in range(0,):
		# 	pyrosim.Send_Motor_Neuron( name = count , jointName = "Tail" + str(y+1) + "_" + "Tail" + str(y+2))




		

		# pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		# pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		# pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
		# pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
		# pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
		# pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
		# pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "LeftCornerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "RightCornerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "FrontCornerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 12, linkName = "BackCornerLeg")


		# pyrosim.Send_Sensor_Neuron(name = 13 , linkName = "LeftCornerLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 14 , linkName = "RightCornerLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 15 , linkName = "FrontCornerLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 16 , linkName = "BackCornerLowerLeg")













		# pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Torso_BackLeg")
		# pyrosim.Send_Motor_Neuron( name = 18 , jointName = "Torso_FrontLeg")
		# pyrosim.Send_Motor_Neuron( name = 19 , jointName = "Torso_LeftLeg")
		# pyrosim.Send_Motor_Neuron( name = 20 , jointName = "Torso_RightLeg")
		# pyrosim.Send_Motor_Neuron( name = 21 , jointName = "FrontLeg_FrontLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 22 , jointName = "BackLeg_BackLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 23 , jointName = "LeftLeg_LeftLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 24 , jointName = "RightLeg_RightLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 25 , jointName = "Torso_LeftCornerLeg")
		# pyrosim.Send_Motor_Neuron( name = 26 , jointName = "Torso_RightCornerLeg")
		# pyrosim.Send_Motor_Neuron( name = 27 , jointName = "LeftCornerLeg_LeftCornerLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 28 , jointName = "RightCornerLeg_RightCornerLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 29 , jointName = "FrontCornerLeg_FrontCornerLowerLeg")
		# pyrosim.Send_Motor_Neuron( name = 30 , jointName = "BackCornerLeg_BackCornerLowerLeg")









		for currentRow in range(0,numSensorNeurons):
			for currentColumn in range(0,numMotorNeurons):
					pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+numSensorNeurons , weight = self.weights[currentRow][currentColumn])



		# pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 2.0 )
		# pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
		# pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 0.5 )
		# pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )

		pyrosim.End()



	