import numpy
import matplotlib.pyplot as plt


frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")

print(frontLegSensorValues)

# plt.plot(frontLegSensorValues, label = "Front Leg", linewidth = 5)
# plt.plot(backLegSensorValues, label = "Back Leg")
# plt.matplotlib.pyplot.legend()


# 

targetAngleValues_BackLeg = numpy.load("data/targetAngles_BackLeg.npy")
targetAngleValues_FrontLeg = numpy.load("data/targetAngles_FrontLeg.npy")

plt.plot(targetAngleValues_BackLeg, label = "BackLeg", linewidth = 5)
plt.plot(targetAngleValues_FrontLeg, label = "Front Leg", linewidth = 1)
plt.matplotlib.pyplot.legend()
plt.matplotlib.pyplot.show()