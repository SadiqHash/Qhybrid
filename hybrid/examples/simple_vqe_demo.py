from hybrid.variational.vqe import VQE
def run_demo(backend):
    v = VQE(backend=backend)
    return v.run_example(backend)
