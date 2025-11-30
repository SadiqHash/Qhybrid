class SimpleAnsatz:
    def __init__(self, n_qubits=1, num_params=1):
        self.n_qubits = n_qubits
        self.num_params = num_params

    def build(self):
        return {"ansatz": "simple", "n_qubits": self.n_qubits}
