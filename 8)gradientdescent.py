
import matplotlib.pyplot as plt
import numpy as np

def cost_function(x) :
    return (x+3)**2

def gradient(x) :
    return 2*(x+3)

x_values = []
y_values = []
num_iterations = 100

x_initial = 2
x = x_initial
learning_rate = 0.1

for i in range(num_iterations) :
    x_values.append(x)
    y_values.append(cost_function(x))
    x = x - learning_rate * gradient(x)
    print(f'Iteration {i+1} : x Value : {x}, Cost : {cost_function(x)}')
print(f'Optimal x : {x}')

x_coordinates = np.linspace(-5,5,100)
plt.plot(x_coordinates,cost_function(x_coordinates))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function Graph for the Cost Function : (x+3)^2 ")
plt.plot(2,cost_function(2),'ro')
plt.show()

plt.plot(x_coordinates,cost_function(x_coordinates))
plt.plot(x_values,y_values,'ro-')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gradient Descent for the Cost Function : (x+3)^2 ")
plt.show()