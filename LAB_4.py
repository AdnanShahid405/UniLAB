import numpy as np
import matplotlib.pyplot as plt
x = np.array([2,3,4,5,6,7])
y = np.array([60,70,80,85,90,95])

print(f"Hours Studied: {x}\nFinal Exam Score: {y}")
xMean = np.mean(x)
yMean = np.mean(y)
print(f"xMean: {xMean}\nyMean: {yMean}")
covXY = 0
varX = 0

n = len(x) # we need this as required to iterate n times

for i in range(n):
    covXY += (x[i] - xMean) * (y[i] - yMean)
    varX += (x[i] - xMean)**2

m = covXY / varX
print(covXY)
print(varX)
print(f"Slope: {m}")
c = yMean - (m * xMean)
print(f"c:{c}")
yPredict = m*x + c
print(yPredict)
plt.scatter(x,y, color = "#e91e63", label = "Scatter")
plt.xlabel("Hours Studied")
plt.ylabel("Final Exam Score")
plt.scatter(x,yPredict, color = "#00b8d4", label = "line")
plt.legend()
plt.show()
plt.plot(x,y, label ="Scatter")
plt.plot(x,yPredict, label = "Line")
plt.legend()
plt.show()
rNum = 0
rDen = 0

for i in range(n):
    rNum += (yPredict[i] - yMean)**2
    rDen += (y[i] - yMean)**2

r = rNum / rDen

print(f"R Square: {r}")
print(f"Accuracy is: {round(r*100)}%")
print(f"Error: {round(100-r*100)}%")