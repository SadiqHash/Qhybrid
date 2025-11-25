class QiskitBackend:
    """Minimal Qiskit backend stub."""
    def __init__(self):
        self.name = "qiskit"

    def run(self, circuit):
        """Run a circuit (not implemented)."""
        raise NotImplementedError("Qiskit backend run() is not implemented yet.")

    def info(self):
        return {"backend": self.name}
