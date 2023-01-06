import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
height = 1
width = 1

x_1 = 0
y_1 = 0
z_1 = 1


for z in range(0,5):
	for y in range(0,5):
		for x in range(0,10):
			pyrosim.Send_Cube(name ="Box", pos=[x_1,y_1,z_1], size=[length, width, height])
			width = .9 * width
			height = .9 * height
			length = .9 * length
			z_1 = z_1 + height
		length = 1
		height = 1
		width = 1
		x_1 = x_1 + 1
		z_1=1
	length = 1
	height = 1
	width = 1
	y_1 = y_1 + 1
	z_1=1
	x_1 = 0


pyrosim.End()