import argparse
from quantum.qiskit_backend import QiskitBackend
from quantum.cirq_backend import CirqBackend
from hybrid.variational.vqe import VQE

def main():
    parser = argparse.ArgumentParser(description="QHybrid CLI: Run quantum-classical simulations")
    parser.add_argument("--backend", choices=["qiskit", "cirq"], default="qiskit", help="Select quantum backend")
    parser.add_argument("--run-demo", action="store_true", help="Run a simple hybrid demo")

    args = parser.parse_args()

    if args.backend == "qiskit":
        backend = QiskitBackend()
    else:
        backend = CirqBackend()

    print(f"Using backend: {args.backend}")

    if args.run_demo:
        print("Running hybrid VQE demo...")
        demo = VQE()
        demo.run_example(backend)
        print("Demo finished!")

if __name__ == "__main__":
    main()
