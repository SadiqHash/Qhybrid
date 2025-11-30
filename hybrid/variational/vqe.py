class VQE:
    """Tiny VQE skeleton to be expanded later."""
    def __init__(self, backend=None, optimizer=None):
        self.backend = backend
        self.optimizer = optimizer

    def run(self, problem_hamiltonian, ansatz, n_iters=1):
        """Run a naive hybrid loop (placeholder)."""
        params = [0.0] * len(getattr(ansatz, "num_params", [0]))
        for _ in range(n_iters):
            energy = 0.0
            # optimizer step would update params
        return {"params": params, "energy": energy}

    def run_example(self, backend):
        return {"status": "ok", "backend": getattr(backend, "name", None)}
