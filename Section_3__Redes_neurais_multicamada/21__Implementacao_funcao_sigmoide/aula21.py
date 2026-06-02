"""
y = 1 / 1 + e**-x
"""

import numpy as np

def sigmoid(soma):
	return 1 / (1 + np.exp(-soma))


a = np.exp(1)
print(a)

a = np.exp(2)
print(a)

a = np.exp(0)
print(a)

a = np.exp(-1)
print(a)

a = sigmoid(0)
print(a)
