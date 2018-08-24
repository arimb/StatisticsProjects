import numpy as np

inputs = np.array([[0,0,1],
                   [1,0,0],
                   [1,1,0],
                   [0,0,1]])
outputs = np.array([0, 1, 1, 0]).T

np.random.seed(1)
weights = 2 * np.random.random((3, 1)) - 1

for i in range(10000):
    output = 1/(1+np.exp(-1*np.dot(inputs, weights)))
    weights += np.dot(inputs.T, (outputs-output)*output*(1-output))

print(1/(1+np.exp(-1*np.dot(np.array([1,1,1]), weights))))