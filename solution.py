import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time

numSensorNeurons = 1
numMotorNeurons = 1
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


		pyrosim.Start_URDF("body.urdf")
		rand_Necks = 3
		rand_Hands = 5
		rand_Hands_y = random.randint(0,5)


		pyrosim.Send_Cube(name="Head", pos=[0, 0, 1], size=[1, 1, 1], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
		
		pyrosim.Send_Joint(name="Head_Neckr1", parent="Head",child="Neckr1", type="revolute", position=[0.25, 0, 1.5],jointAxis = "0 0 1",rpy = -1)
		pyrosim.Send_Cube(name="Neckr1", pos=[0, 0, .2], size=[.4, .4, .4], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')
		
		pyrosim.Send_Joint(name="Head_Neckl1", parent="Head",child="Neckl1", type="revolute", position=[-.25, 0, 1.5],jointAxis = "0 0 1",rpy = 1)
		pyrosim.Send_Cube(name="Neckl1", pos=[0, 0, .2], size=[.4, .4, .4], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')
		
		pyrosim.Send_Joint(name="Head_Hand1", parent="Head",child="Hand1", type="revolute", position=[0.5, 0, 1],jointAxis = "1 0 0",rpy = 0)
		pyrosim.Send_Cube(name="Hand1", pos=[.25, 0, 0], size=[.5,.5,.5], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')
		
		pyrosim.Send_Joint(name="Head_Tail1", parent="Head",child="Tail1", type="revolute", position=[0, -.50, 1],jointAxis = "1 0 0",rpy = 0)
		pyrosim.Send_Cube(name="Tail1", pos=[0, -.3, 0], size=[.6,.6,.6], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')

		pyrosim.Send_Joint(name="Head_Tailb1", parent="Head",child="Tailb1", type="revolute", position=[0, .50, 1],jointAxis = "1 0 0",rpy = 0)
		pyrosim.Send_Cube(name="Tailb1", pos=[0, .3, 0], size=[.6,.6,.6], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 255 1.0"/>')
		x = 1
		count_necks = 0
		count_green = 1

		prev_dimension = 0.4
		while count_necks < rand_Necks:
			green = random.randint(0,1)
			dimension = random.random() * 0.5
			dimension_x = random.random()

			print("countnecks: ",count_necks)
			if(green):# and count_green < numSensorNeurons):
		 		count_green+=1
		 		self.links_with_sensors[x] = "Neck" + str(x) 
		 		pyrosim.Send_Joint(name="Neckr" + str(x) + "_" + "Neckr" + str(x+1), parent="Neckr" + str(x), child="Neckr" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy =0)
		 		pyrosim.Send_Cube(name="Neckr"+str(x+1), pos=[0, 0, dimension/2], size=[dimension_x,.6,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
			else:
		 		pyrosim.Send_Joint(name="Neckr" + str(x) + "_" + "Neckr" + str(x+1), parent="Neckr" + str(x), child="Neckr" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy = 0)
		 		pyrosim.Send_Cube(name="Neckr"+str(x+1), pos=[0, 0, dimension/2], size=[dimension_x,.6,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			prev_dimension = dimension
			count_necks+=1
			x+=1


		x = 1
		count_necks = 0
		count_green = 1

		prev_dimension = 0.4
		while count_necks < rand_Necks:
			green = random.randint(0,1)
			dimension = random.random() * 0.5
			dimension_x = random.random() 
 
			print("countnecks: ",count_necks)
			if(green):# and count_green < numSensorNeurons):
		 		count_green+=1
		 		self.links_with_sensors[x] = "Neck" + str(x) 
		 		pyrosim.Send_Joint(name="Neckl" + str(x) + "_" + "Neckl" + str(x+1), parent="Neckl" + str(x), child="Neckl" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy =0)
		 		pyrosim.Send_Cube(name="Neckl"+str(x+1), pos=[0, 0, dimension/2], size=[dimension_x,.6,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
			else:
		 		pyrosim.Send_Joint(name="Neckl" + str(x) + "_" + "Neckl" + str(x+1), parent="Neckl" + str(x), child="Neckl" + str(x+1), type="revolute", position=[0, 0, prev_dimension],jointAxis = "0 0 1",rpy = 0)
		 		pyrosim.Send_Cube(name="Neckl"+str(x+1), pos=[0, 0, dimension/2], size=[dimension_x,.6,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			prev_dimension = dimension
			count_necks+=1
			x+=1
			
		x = 1
		count_hands= 0
		count_green = 1

		prev_dimension = 0.5
		while count_hands < rand_Hands:
			green = random.randint(0,1)
			dimension = random.random() *.2

			if(green):# and count_green < numSensorNeurons):
		 		count_green+=1
		# 		#self.links_with_sensors[x] = "Neck" + str(x) 
		 		pyrosim.Send_Joint(name="Hand" + str(x) + "_" + "Hand" + str(x+1), parent="Hand" + str(x), child="Hand" + str(x+1), type="revolute", position=[prev_dimension, 0, 0],jointAxis = "1 0 0",rpy =random.randint(0,1))
		 		pyrosim.Send_Cube(name="Hand"+str(x+1), pos=[dimension/2, 0, 0], size=[dimension,dimension,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
			else:
		 		pyrosim.Send_Joint(name="Hand" + str(x) + "_" + "Hand" + str(x+1), parent="Hand" + str(x), child="Hand" + str(x+1), type="revolute", position=[prev_dimension, 0, 0],jointAxis = "1 0 0",rpy = random.randint(0,1))
		 		pyrosim.Send_Cube(name="Hand"+str(x+1), pos=[dimension/2, 0, 0], size=[dimension,dimension,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			prev_dimension = dimension
			count_hands+=1
			x+=1


		x = 1
		count_tails= 0
		count_green = 1

		prev_dimension = 0.5
		while count_tails < 25:
			green = random.randint(0,1)
			dimension = random.random()/3

			if(green):# and count_green < numSensorNeurons):
		 		count_green+=1
		 		self.links_with_sensors[x] = "Neck" + str(x) 
		 		pyrosim.Send_Joint(name="Tail" + str(x) + "_" + "Tail" + str(x+1), parent="Tail" + str(x), child="Tail" + str(x+1), type="revolute", position=[0,-prev_dimension,  0],jointAxis = "1 0 0",rpy =0)
		 		pyrosim.Send_Cube(name="Tail"+str(x+1), pos=[0,-dimension/2, 0], size=[dimension,dimension,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
			else:
		 		pyrosim.Send_Joint(name="Tail" + str(x) + "_" + "Tail" + str(x+1), parent="Tail" + str(x), child="Tail" + str(x+1), type="revolute", position=[0,-prev_dimension, 0],jointAxis = "1 0 0",rpy = 0)
		 		pyrosim.Send_Cube(name="Tail"+str(x+1), pos=[0,-dimension/2,  0], size=[dimension,dimension,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			prev_dimension = dimension
			count_tails+=1
			x+=1

		pyrosim.Send_Joint(name="Tail" + str(x) + "_" + "Tail" + str(x+1), parent="Tail" + str(x), child="Tail" + str(x+1), type="revolute", position=[-prev_dimension, 0, 0],jointAxis = "1 0 0",rpy = -1)
		pyrosim.Send_Cube(name="Tail"+str(x+1), pos=[-dimension/2, 0, 0], size=[dimension,dimension,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
		

		x = 1
		count_tails= 0
		count_green = 1

		prev_dimension = 0.5
		while count_tails < 15:
			green = random.randint(0,1)
			dimension = random.random()/3

			if(green):# and count_green < numSensorNeurons):
		 		count_green+=1
		 		self.links_with_sensors[x] = "Neck" + str(x) 
		 		pyrosim.Send_Joint(name="Tailb" + str(x) + "_" + "Tailb" + str(x+1), parent="Tailb" + str(x), child="Tailb" + str(x+1), type="revolute", position=[0,prev_dimension,  0],jointAxis = "1 0 0",rpy =0)
		 		pyrosim.Send_Cube(name="Tailb"+str(x+1), pos=[0,dimension/2, 0], size=[dimension,dimension,dimension], color_name = "Green",rgb_color_string = '    <color rgba="0 255 0 1.0"/>')
			else:
		 		pyrosim.Send_Joint(name="Tailb" + str(x) + "_" + "Tailb" + str(x+1), parent="Tailb" + str(x), child="Tailb" + str(x+1), type="revolute", position=[0,prev_dimension, 0],jointAxis = "1 0 0",rpy = 0)
		 		pyrosim.Send_Cube(name="Tailb"+str(x+1), pos=[0,dimension/2,  0], size=[dimension,dimension,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
			prev_dimension = dimension
			count_tails+=1
			x+=1

		pyrosim.Send_Joint(name="Tailb" + str(x) + "_" + "Tailb" + str(x+1), parent="Tailb" + str(x), child="Tailb" + str(x+1), type="revolute", position=[-prev_dimension, 0, 0],jointAxis = "1 0 0",rpy = -1)
		pyrosim.Send_Cube(name="Tailb"+str(x+1), pos=[dimension/2, 0, 0], size=[dimension,dimension,dimension], color_name = "Blue",rgb_color_string = '    <color rgba="0 0 225 1.0"/>')
		pyrosim.End()



	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

		pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Head")
		pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Neck")
		pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Tail")
		count = 1
		for key in self.links_with_sensors.keys():
		 	pyrosim.Send_Sensor_Neuron(name = count , linkName = "Neck" + str(key))
		 	count+=1
		print(self.links_with_sensors)
		print("count:", count)




		pyrosim.Send_Motor_Neuron( name = 1 , jointName = "Head_Neckr1")
		pyrosim.Send_Motor_Neuron( name = count+1 , jointName = "Head_Tail")
		pyrosim.Send_Motor_Neuron( name = count+2 , jointName = "Tail_Tail1")


		for y in range(0,):
			pyrosim.Send_Motor_Neuron( name = count , jointName = "Tail" + str(y+1) + "_" + "Tail" + str(y+2))




		

	








		for currentRow in range(0,numSensorNeurons):
			for currentColumn in range(0,numMotorNeurons):
					pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+numSensorNeurons , weight = self.weights[currentRow][currentColumn])



		# pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 2.0 )
		# pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
		# pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 0.5 )
		# pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )

		pyrosim.End()



	