import numpy as np

def bra_str(state):
	return '<' + state + '|'

def ket_str(state):
	return '|' + state + '>'

def normalize(arr):
	assert type(arr) == np.ndarray, "arr must be array-like"
	norm = np.linalg.norm(arr)
	assert norm != 0, "norm cannot be 0"

	return arr / np.linalg.norm(arr)

class qstate:
	def __init__(self, amplitudes=np.array((1+0j, 0j))):
		assert type(amplitudes) == np.ndarray, "amplitudes must be array-like"
		self.amplitudes = normalize(amplitudes)