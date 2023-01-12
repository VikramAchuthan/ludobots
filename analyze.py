import numpy
import matplotlib.pyplot as plt


frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")

print(frontLegSensorValues)

plt.plot(frontLegSensorValues, label = "Front Leg", linewidth = 5)
plt.plot(backLegSensorValues, label = "Back Leg")
plt.matplotlib.pyplot.legend()


plt.matplotlib.pyplot.show()

