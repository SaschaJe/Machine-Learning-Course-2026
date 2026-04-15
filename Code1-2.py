from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x = np.array([21, 18, 15, 8, 8, 1.5 ,0]).reshape(-1,1)  #features

y = np.array([81, 69, 29, 41, 44, 8, 10]) #labels

model = LinearRegression()
model.fit(x, y)

a = model.coef_[0] # slope
b = model.intercept_
error = np.mean((model.predict(x) - y)**2) # mean squared error
print(error)

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, model.predict(x), color='red', label='Best Fit Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('SklearnLinear Regression: Hours Studied vs Exam Score')
plt.legend()
plt.show()
