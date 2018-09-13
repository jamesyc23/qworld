from qtools import *
from qgates import *

# Describes the state of a quantum system
class qstate:
	def __init__(self, amplitudes=np.array((1, 0))):
		assert type(amplitudes) == np.ndarray, "amplitudes must be a numpy array"
		assert int(log(len(amplitudes), 2)) == log(len(amplitudes), 2), "number of amplitudes given must be a power of 2"
		self.amplitudes = normalize(amplitudes)
		self.num_qubits = int(log(len(amplitudes), 2))

	# Measures the quantum state in the logical bases
	def measure(self, num_samples):
		assert type(num_samples) == int, "num_samples must be an integer"
		probs = np.real(np.conjugate(self.amplitudes)*self.amplitudes)
		return np_bin(np.random.choice(len(self.amplitudes), num_samples, p=probs), width=self.num_qubits)

	# TODO
	def act(self, gate, qubits=(0)):
		assert type(gate) == np.ndarray, "gate must be a numpy array"
		assert len(gate.shape) == 2, "gate must be two dimensional"
		# TODO
		self.amplitudes = np.dot(gate, self.amplitudes)

# Gets a quantum system with n qubits, all in the 0 state
def get_initial_state(n):
	assert type(n) == int, "n must be an integer"
	amplitudes = np.zeros(2 ** n)
	amplitudes[0] = 1
	return qstate(amplitudes)

# Gets a quantum system with the basis vector corresponding to the binary string s
def get_basis_state(s):
	assert type(s) == str, "state must be a string"
	index = int(s, 2)
	amplitudes = np.zeros(2 ** len(s))
	amplitudes[index] = 1
	return qstate(amplitudes)

# Gets a quantum system with n qubits, each with identical, real amplitudes
def get_equal_state(n):
	assert type(n) == int, "n must be an integer"
	amplitudes = np.ones(2 ** n)
	amplitudes = normalize(amplitudes)
	return qstate(amplitudes)

# Gets a quantum system with n qubits in a superposition of all 0 and all 1 states
def get_cat_state(n):
	assert type(n) == int, "n must be an integer"
	amplitudes = np.zeros(2 ** n)
	amplitudes[0], amplitudes[-1] = 1, 1
	amplitudes = normalize(amplitudes)
	return qstate(amplitudes)
