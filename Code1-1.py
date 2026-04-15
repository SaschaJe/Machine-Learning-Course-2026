import numpy as np
import matplotlib.pyplot as plt

# Collect data from exercise sheet:

x = np.array([21, 18, 15, 8, 8, 1.5 ,0])  #features

y = np.array([81, 69, 29, 41, 44, 8, 10]) #labels

x_mean = np.mean(x) #mean of x
y_mean = np.mean(y) #mean of y

a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2) # slope
b = y_mean - a*x_mean

y_pred = a*x + b

error = np.sum((y - y_pred)**2) / len(x) # mean squared error
print(error)

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, [a*xi + b for xi in x], color='red', label='Best Fit Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Manual Linear Regression: Hours Studied vs Exam Score')
plt.legend()
plt.show()
