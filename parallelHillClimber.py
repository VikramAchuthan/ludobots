from solution import SOLUTION
import os

numberOfGenerations = 2
populationSize = 2
import copy

class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		os.system("rm brain*.nndf")
		os.system("rm fitness*.txt")

		self.parents = {}
		self.nextAvailableID = 0

		for x in range(0, populationSize):
			self.parents[x] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID += 1




	def Evaluate(self, solutions):
		for x in range(0, populationSize):
			solutions[x].Start_Simulation("DIRECT")
		for x in range(0, populationSize):
			solutions[x].Wait_For_Simulation_To_End("rm fitness" + str(x) + ".txt")



	def Evolve(self):

		self.Evaluate(self.parents)

		for currentGeneration in range(0, numberOfGenerations):
			self.Evolve_For_One_Generation()
			
	def Evolve_For_One_Generation(self):
		
		self.Spawn()

		self.Mutate()

		self.Evaluate(self.children)
		self.Print()
		
		self.Select()

	def Print(self):
		for key in self.parents.keys():
			print("parent fitness: ", self.parents[key].fitness, "child fitness: ", self.children[key].fitness)
			print("  ")

	def Spawn(self):
		self.children = {}
		for key in self.parents.keys():
			self.children[key] = copy.deepcopy(self.parents[key])
			self.children[key].Set_ID(self.nextAvailableID)
			self.nextAvailableID +=1


	def Mutate(self):
		for key in self.children.keys(): 
			self.children[key].Mutate()

		
		
	def Select(self):
		for key in self.parents.keys():
			if self.parents[key].fitness > self.children[key].fitness:
				self.parents[key] = self.children[key]
	
	def Show_Best(self):
		smallest_fitness = self.parents[0].fitness
		smallest_fitness_parent = self.parents[0]
		for key in self.parents.keys():
			if self.parents[key].fitness < smallest_fitness:
				smallest_fitness = self.parents[key].fitness
				smallest_fitness_parent = self.parents[key]

		smallest_fitness_parent.Start_Simulation("GUI")


