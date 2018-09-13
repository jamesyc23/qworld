from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import X, H, CNOT, Z
from bell_states import phi_plus

qvm = QVMConnection(use_queue=True)

def teleport (s, a, r):
	p = Program() + phi_plus(a, r)
	p.inst(CNOT(s, a))
	p.inst(H(s))

	p.measure(a, 0)
	p.measure(s, 1)

	p.if_then(1, X(2))
	p.if_then(0, Z(2))

	return p