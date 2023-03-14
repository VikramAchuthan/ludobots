import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time

numSensorNeurons = 7
numMotorNeurons = 6

class SOLUTION:

	def __init__(self, next_id):

		self.weights = 2*numpy.random.rand(numSensorNeurons,numMotorNeurons)-1
		self.myID = next_id
		self.last_leg_num = 0
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
		#random.seed(5) #start from 5, increase using fibanocci series (8,13...)
		pyrosim.Start_URDF('body' + str(self.myID) + '.urdf')
		#pyrosim.Start_URDF("body.urdf")
		length = 1
		height = 1
		width = 1

		x_1 = 1
		y_1 = 0
		z_1 = 0.5


		random_torso_y = random.random()
		random_torso_x = random.random()*1.3
		pyrosim.Send_Cube(name ="Torso", pos=[0,0,1], size=[random_torso_x, random_torso_y, 1], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')


		
		pyrosim.Send_Joint(name="Torso_Neckr1", parent="Torso",child="Neckr1", type="revolute", position=[0.25, 0, 1.5],jointAxis = "0 0 1",rpy = -1)
		pyrosim.Send_Cube(name="Neckr1", pos=[0, 0, .2], size=[.4, .4, .4], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')

		if random.randint(1,3) == 3:

			pyrosim.Send_Joint(name="Torso_Neckl1", parent="Torso",child="Neckl1", type="revolute", position=[-.25, 0, 1.5],jointAxis = "0 0 1",rpy = 1)
			pyrosim.Send_Cube(name="Neckl1", pos=[0, 0, .2], size=[.4, .4, .4], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')




		rpy_rand = random.randint(0,2)

		pyrosim.Send_Joint( name = "Torso_FrontLeg1" , parent= "Torso" , child = "FrontLeg1" , 
			type = "revolute", position = [0,random_torso_y/4,1], jointAxis = "0 1 0",rpy = 0)
		pyrosim.Send_Cube(name ="FrontLeg1", pos=[0,.5,0], size=[random_torso_y/2,1,random_torso_y/2],color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')
		
		rpy_rand = random.randint(-1,1)

		random_lower_front_leg = random.random()/3

		pyrosim.Send_Joint( name = "FrontLeg1_FrontLowerLeg" , parent= "FrontLeg1" , child = "FrontLowerLeg" , 
			type = "revolute", position = [0,1 + random_lower_front_leg,0], jointAxis = "0 1 0",rpy = 0)
		pyrosim.Send_Cube(name ="FrontLowerLeg", pos=[0,0,-0.5], size=[random_lower_front_leg*2,random_lower_front_leg*2,1], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')



		pyrosim.Send_Joint( name = "Torso_BackLeg1" , parent= "Torso" , child = "BackLeg1" , 
			type = "revolute", position = [0,-random_torso_y/4,1], jointAxis = "0 1 0", rpy = 0)
		pyrosim.Send_Cube(name ="BackLeg1", pos=[0,-.5,0], size=[random_torso_y/2,1,random_torso_y/2], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')
		
		random_lower_back_leg = random.random()/3

		pyrosim.Send_Joint( name = "BackLeg1_BackLowerLeg" , parent= "BackLeg1", child = "BackLowerLeg" , 
			type = "revolute", position = [0,-1 - random_lower_back_leg,0], jointAxis = "0 1 0", rpy = 0)
		pyrosim.Send_Cube(name ="BackLowerLeg", pos=[0,0,-0.5], size=[random_lower_back_leg,random_lower_back_leg*2,1], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')

		left_leg_bool = random.randint(0,1)
		if left_leg_bool == 1:
			pyrosim.Send_Joint( name = "Torso_LeftLeg1" , parent= "Torso" , child = "LeftLeg1" , 
				type = "revolute", position = [-random_torso_x/4,0,1], jointAxis = "0 1 0",rpy = 0)
			pyrosim.Send_Cube(name ="LeftLeg1", pos=[-0.5,0,0], size=[1.0,0.2,0.2], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')

			x = 1
			count_legs = 0
			random_legs = random.randint(1,5)
			self.last_leg_num  = random_legs + 1
			prev_dimension = 0.4
			while count_legs < random_legs:
				green = random.randint(0,1)
				dimension = random.random() /3
				dimension_x = random.random()/3

				#print("countnecks: ",count_necks)
				if(green):# and count_green < numSensorNeurons):
			 		pyrosim.Send_Joint(name="LeftLeg" + str(x) + "_" + "LeftLeg" + str(x+1), parent="LeftLeg" + str(x), child="LeftLeg" + str(x+1), type="revolute", position=[-prev_dimension, 0, 0],jointAxis = "1 0 0",rpy =0)
			 		pyrosim.Send_Cube(name="LeftLeg"+str(x+1), pos=[-dimension/2, 0, 0], size=[dimension,.6,.7], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
				else:
			 		pyrosim.Send_Joint(name="LeftLeg" + str(x) + "_" + "LeftLeg" + str(x+1), parent="LeftLeg" + str(x), child="LeftLeg" + str(x+1), type="revolute", position=[-prev_dimension, 0, 0],jointAxis = "1 0 0",rpy = 0)
			 		pyrosim.Send_Cube(name="LeftLeg"+str(x+1), pos=[-dimension/2, 0, 0], size=[dimension,0.6,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
				prev_dimension = dimension
				count_legs+=1
				x+=1
			pyrosim.Send_Joint( name = "LeftLeg" + str(random_legs + 1) + "_LeftLowerLeg" , parent= "LeftLeg" + str(random_legs + 1)  , child = "LeftLowerLeg" , 
				type = "revolute", position = [-.1,0,0], jointAxis = "0 1 0",rpy = 0)
			pyrosim.Send_Cube(name ="LeftLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
		else:
			self.last_leg_num = 0
		# pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , 
		# 	type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0",rpy = -1)
		# pyrosim.Send_Cube(name ="RightLeg", pos=[0.5,0,0], size=[1.0,0.2,0.2], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')


		# pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , 
		# 	type = "revolute", position = [1.1,0,0], jointAxis = "0 1 0",rpy = 0)
		# pyrosim.Send_Cube(name ="RightLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1],color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
		# count_necks = 0
		# count_green = 0
		# x = 1
		# prev_dimension = 1
		# while count_necks < 3:
		# 	green = random.randint(0,1)
		# 	dimension = random.random() * 0.2

		# 	#print("countnecks: ",count_necks)
		# 	if(green):# and count_green < numSensorNeurons):
		#  		count_green+=1
		#  		pyrosim.Send_Joint(name="FrontLeg" + str(x) + "_" + "FrontLeg" + str(x+1), parent="FrontLeg" + str(x), child="FrontLeg" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy =0)
		#  		pyrosim.Send_Cube(name="FrontLeg"+str(x+1), pos=[0, 0, dimension/2], size=[dimension,.5,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
		# 	else:
		#  		pyrosim.Send_Joint(name="FrontLeg" + str(x) + "_" + "FrontLeg" + str(x+1), parent="FrontLeg" + str(x), child="FrontLeg" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy = 0)
		#  		pyrosim.Send_Cube(name="FrontLeg"+str(x+1), pos=[0, 0, dimension/2], size=[dimension,.5,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
		# 	prev_dimension = dimension
		# 	count_necks+=1
		# 	x+=1
		

		x = 1
		rand_Necks = 10
		count_necks = 0
		count_green = 1

		prev_dimension = 0.4
		while count_necks < 3:
			green = random.randint(0,1)
			dimension = random.random() * 0.2
			dimension_x = random.random()

			#print("countnecks: ",count_necks)
			if(green):# and count_green < numSensorNeurons):
		 		count_green+=1
		 		pyrosim.Send_Joint(name="Neckr" + str(x) + "_" + "Neckr" + str(x+1), parent="Neckr" + str(x), child="Neckr" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy =0)
		 		pyrosim.Send_Cube(name="Neckr"+str(x+1), pos=[0, 0, dimension/2], size=[dimension,dimension,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
			else:
		 		pyrosim.Send_Joint(name="Neckr" + str(x) + "_" + "Neckr" + str(x+1), parent="Neckr" + str(x), child="Neckr" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy = 0)
		 		pyrosim.Send_Cube(name="Neckr"+str(x+1), pos=[0, 0, dimension/2], size=[dimension,dimension,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			prev_dimension = dimension
			count_necks+=1
			x+=1

		# x = 1
		# count_necks = 0
		# count_green = 1

		# prev_dimension = 0.4
		# while count_necks < rand_Necks:
		# 	green = random.randint(0,1)
		# 	dimension = random.random() * 0.2
		# 	dimension_x = random.random() 
 
		# 	#print("countnecks: ",count_necks)
		# 	if(green):# and count_green < numSensorNeurons):
		#  		count_green+=1
		#  		pyrosim.Send_Joint(name="Neckl" + str(x) + "_" + "Neckl" + str(x+1), parent="Neckl" + str(x), child="Neckl" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy =0)
		#  		pyrosim.Send_Cube(name="Neckl"+str(x+1), pos=[0, 0, dimension/2], size=[dimension_x,.6,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
		# 	else:
		#  		pyrosim.Send_Joint(name="Neckl" + str(x) + "_" + "Neckl" + str(x+1), parent="Neckl" + str(x), child="Neckl" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy = 0)
		#  		pyrosim.Send_Cube(name="Neckl"+str(x+1), pos=[0, 0, dimension/2], size=[dimension_x,.6,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
		# 	prev_dimension = dimension
		# 	count_necks+=1
		# 	x+=1







		
		pyrosim.End()
	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg1")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg1")
		
		# pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
		pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLowerLeg")
		pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "BackLowerLeg")
		# pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
		if self.last_leg_num != 0:
			pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LeftLeg1")

			pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LeftLowerLeg")


			pyrosim.Send_Motor_Neuron( name = 7, jointName = "Torso_BackLeg1")

			pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_FrontLeg1")

			pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_LeftLeg1")
			# pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
			pyrosim.Send_Motor_Neuron( name = 10 , jointName = "FrontLeg1_FrontLowerLeg")
			pyrosim.Send_Motor_Neuron( name = 11 , jointName = "BackLeg1_BackLowerLeg")
			pyrosim.Send_Motor_Neuron( name = 12 , jointName = "LeftLeg" + str(self.last_leg_num) + "_LeftLowerLeg")
			numSensorNeurons = 7
			numMotorNeurons = 6
		else:

			pyrosim.Send_Motor_Neuron( name = 5, jointName = "Torso_BackLeg1")
			pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_FrontLeg1")
			#pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_LeftLeg1")
			# pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
			pyrosim.Send_Motor_Neuron( name = 7 , jointName = "FrontLeg1_FrontLowerLeg")
			pyrosim.Send_Motor_Neuron( name = 8 , jointName = "BackLeg1_BackLowerLeg")
			numSensorNeurons = 5
			numMotorNeurons = 4

		# pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg")






		for currentRow in range(0,numSensorNeurons):
			for currentColumn in range(0,numMotorNeurons):
					pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+numSensorNeurons , weight = self.weights[currentRow][currentColumn])



	

		pyrosim.End()