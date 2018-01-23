from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import X, H, CNOT

qvm = QVMConnection(use_queue=True)

def phi_plus(p, q0, q1):
	"""Initiate phi plus Bell state between qubits q0 and q1 of Program p."""
	p.inst(H(q0), CNOT(q0, q1))

def phi_minus(p, q0, q1):
	"""Initiate phi minus Bell state between qubits q0 and q1 of Program p."""
	p.inst(X(q0), H(q0), CNOT(q0, q1))

def psi_plus(p, q0, q1):
	"""Initiate psi plus Bell state between qubits q0 and q1 of Program p."""
	p.inst(X(q1), H(q0), CNOT(q0, q1))

def psi_minus(p, q0, q1):
	"""Initiate psi minus Bell state between qubits q0 and q1 of Program p."""
	p.inst(X(q0), X(q1), H(q0), CNOT(q0, q1))

# wavefunction = qvm.wavefunction(p)
# print(wavefunction)