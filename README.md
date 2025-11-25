QHybrid

A Quantum + Classical Hybrid Simulator that lets developers build, run, and experiment with hybrid quantum algorithms using Qiskit, Cirq, and Python classical processing. QHybrid is built version by version with a clean backend only architecture, meant to grow into a full open‑source toolkit for hybrid computing.

This first version focuses on three powerful features:

* Qiskit + Cirq backends (fully modular)
* Translator  between Qiskit ↔ Cirq circuit formats
* Variational Framework (VQE engine)
* Notebook templates for learning and experimentation

---

🌌 What QHybrid Is

QHybrid is a backend framework for developers, students, and researchers who want to:

* Build quantum circuits programmatically
* Mix classical and quantum logic cleanly
* Run circuits on Qiskit or Cirq simulators
* Experiment with variational algorithms (VQE)
* Translate circuits between frameworks
* Understand hybrid computing through notebooks.

Instead of hiding complexity, QHybrid shows you how hybrid computing really works under the hood.

---

📁 Project Structure

Below is the final structure for QHybrid v1.

```
qhybrid/
│
├── quantum/
│   ├── qiskit_backend.py
│   ├── cirq_backend.py
│   ├── circuit_builder.py
│   ├── gate_library.py
│   ├── executor.py
│   └── translator.py
│
├── classical/
│   ├── key_strength.py
│   └── utils.py
│
├── hybrid/
│   ├── variational/
│   │   ├── vqe.py
│   │   ├── ansatz_library.py
│   │   ├── optimizers.py
│   │   └── cost_functions.py
│   └── examples/
│       ├── hybrid_hello_world.py
│       └── simple_vqe_demo.py
│
├── visualize/
│   ├── circuit_drawer.py
│   └── ascii_drawer.py
│
├── notebooks/
│   ├── 01_introduction.ipynb
│   ├── 02_building_quantum_circuits.ipynb
│   ├── 03_hybrid_workflow.ipynb
│   ├── 04_vqe_example.ipynb
│   └── 05_translate_qiskit_to_cirq.ipynb
│
├── cli/
│   └── main.py
│
├── core/
│   ├── config.py
│   ├── errors.py
│   └── logger.py
│
├── tests/
│
├── README.md
└── pyproject.toml
```
---

🧠 Deep Explanation of Each Important Module

Below is a simple, clear explanation of what each part of QHybrid does.

🔷 `quantum/qiskit_backend.py`

Handles execution of quantum circuits using Qiskit’s Aer simulator.

* Create circuits
* Set up measurement
* Run and get results
* Convert outputs into clean Python structures

🔷 `quantum/cirq_backend.py`

Same purpose as the Qiskit backend but built using Cirq.

* Supports Cirq gates
* Converts back results
* Works as an interchangeable backend

🔷 `quantum/circuit_builder.py`

A unified interface for building circuits.

* Add gates
* Add qubits
* Add classical registers
* Export to either Qiskit or Cirq

🔷 `quantum/gate_library.py`

Defines universal gates used across frameworks:

* X, Y, Z
* H, S, T
* RX, RY, RZ
* CNOT, CZ, SWAP

This ensures consistent gate usage across Qiskit and Cirq.

🔷 `quantum/executor.py`

Central controller for running circuits.

* Chooses backend
* Executes
* Returns formatted results

🔷 `quantum/translator.py`

The Qiskit ↔ Cirq translator.
Converts a circuit built using Qiskit into a Cirq equivalent.

This is one of QHybrid most unique features.

---

🟦 Classical Logic

🔷 `classical/key_strength.py`

Simple quantum‑resistant key analyzer.

* Evaluates RSA / symmetric strength
* Estimates Grover / Shor impact
* Returns a “quantum safety score”.

🔷 `classical/utils.py`

General math helpers.

---

🟩 Hybrid Engine (Variational Framework)

🔷 `hybrid/variational/vqe.py`

Core VQE engine:

* Hybrid loop
* Parameter update
* Energy estimation

🔷 `hybrid/variational/ansatz_library.py`

Templates for variational circuits.

🔷 `hybrid/variational/optimizers.py`

Simple gradient free optimizers.

🔷 `hybrid/variational/cost_functions.py`

Hamiltonians and cost evaluations.

🔷 `hybrid/examples/simple_vqe_demo.py`

A minimal working VQE example.

---

🎨 Visualization Tools

🔷 `visualize/circuit_drawer.py`

Creates clean plots of circuits.

🔷 `visualize/ascii_drawer.py`

Lightweight ASCII circuit rendering for terminal use.

---

📓 Notebooks Folder:

Guides users step by step.

* Intro to quantum circuits
* Building hybrid circuits
* VQE basics
* Translating circuits between frameworks

These notebooks make QHybrid easy to learn and teach.

---

▶️ Running QHybrid

```bash
python -m qhybrid
```

Or open the notebooks:

```bash
jupyter notebook notebooks/
```

---

🛤️ Roadmap

QHybrid grows version by version. Future versions will include:

* API mode
* Quantum cloud execution
* More hybrid algorithms
* Quantum secure encryption
* and more

---

🤝 Contribution

QHybrid is open‑source.
Contributions, feedback, and experiments are always welcome.

---

Final Note

QHybrid is built for developers who want to understand the future of computing.
Hybrid quantum classical logic will power the next era and this project gives you a hands on way to learn it.
