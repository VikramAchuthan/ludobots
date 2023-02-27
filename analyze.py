import numpy
import matplotlib.pyplot as plt

#create fitness graph
data = numpy.load("file1.npy")
data_2 = numpy.load("file2.npy")
data_3 = numpy.load("file3.npy")
data_4 = numpy.load("file4.npy")
data_5 = numpy.load("file5.npy")


xArr = list(range(0,c.numberOfGenerations))
plt.plot(xArr, data, color = "red")
plt.plot(xArr, data_2, color = "blue")
plt.plot(xArr, data_3, color = "green")
plt.plot(xArr, data_4, color = "orange")
plt.plot(xArr, data_5, color = "purple")
plt.xlabel("Number of Generations")
plt.ylabel("Fitness")
plt.legend(['5', '8', '13','21','34'])