import numpy as np
from math import log

# TODO
def bra_str(state):
	return '<' + state + '|'

# TODO
def ket_str(state):
	return '|' + state + '>'

# TODO
def normalize(arr):
	assert type(arr) == np.ndarray, "arr must be array-like"
	norm = np.linalg.norm(arr)
	assert norm != 0, "norm cannot be 0"
	return arr / np.linalg.norm(arr)

np_bin = np.vectorize(np.binary_repr)
pi = np.pi