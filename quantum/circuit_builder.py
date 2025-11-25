class CircuitBuilder:
    """Unified tiny circuit builder interface (placeholder)."""
    def __init__(self):
        self.ops = []

    def add_gate(self, gate, qubits, params=None):
        self.ops.append((gate, qubits, params))

    def export(self, framework="qiskit"):
        """Return a placeholder representation."""
        return {"framework": framework, "ops": list(self.ops)}
