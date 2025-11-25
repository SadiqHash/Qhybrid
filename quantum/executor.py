class Executor:
    """Select backend and call its run()."""
    def __init__(self, backend):
        self.backend = backend

    def execute(self, circuit):
        if not hasattr(self.backend, "run"):
            raise RuntimeError("Backend has no run() method.")
        return self.backend.run(circuit)
