class CirqBackend:
    """Minimal Cirq backend stub."""
    def __init__(self):
        self.name = "cirq"

    def run(self, circuit):
        raise NotImplementedError("Cirq backend run() is not implemented yet.")

    def info(self):
        return {"backend": self.name}
