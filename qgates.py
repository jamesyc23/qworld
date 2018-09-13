from qtools import *

# Returns true if a gate is unitary, false otherwise
def is_unitary(gate):
	assert type(gate) == np.ndarray, "gate must be a numpy array"
	assert len(gate.shape) == 2, "gate must be two dimensional"
	identity = np.eye(gate.shape[0])
	return gate.shape[0] == gate.shape[1] and np.allclose(np.conj(gate.T).dot(gate), identity)

# Single qubit gates
def RX(theta):
	return np.array(((np.cos(theta / 2), np.sin(theta / 2)), (np.sin(theta / 2), np.cos(theta / 2))))

def RY(theta):
	return np.array(((np.cos(theta / 2), -1j * np.sin(theta / 2)), (1j * np.sin(theta / 2), np.cos(theta / 2))))

def RZ(phi):
	return np.array(((1, 0), (0, np.exp(1j * phi))))

I = np.array(((1, 0), (0, 1)))
X = np.array(((0, 1), (1, 0)))
Y = np.array(((0, -1j), (1j, 0)))
Z = np.array(((1, 0), (0, -1)))
H = (2 ** -0.5) * np.array(((1, 1), (1, -1)))

NOT = X

def RX(theta):
	return np.cos(theta / 2) * I - 1j * np.sin(theta / 2) * X

def RY(theta):
	return np.cos(theta / 2) * I - 1j * np.sin(theta / 2) * Y

def RZ(theta):
	return np.cos(theta / 2) * I - 1j * np.sin(theta / 2) * Z

# Two qubit gates
SWAP = np.array(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)))
SQSWAP = np.array(((1, 0, 0, 0), (0, 0.5 * (1 + 1j), 0.5 * (1 - 1j), 0), (0, 0.5 * (1 - 1j), 0.5 * (1 + 1j), 0), (0, 0, 0, 1)))

S = SWAP
SQS = SQSWAP