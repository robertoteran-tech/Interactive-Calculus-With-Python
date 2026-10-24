# Calculus Lab

A learn-by-doing calculus course built with Jupyter notebooks, SymPy, NumPy, and Plotly.

## Course map

| Module | Topic | Notebook |
| --- | --- | --- |
| 1 | Functions and graphs | `notebooks/01_functions_and_graphs.ipynb` |
| 2 | Limits | `notebooks/02_limits.ipynb` |
| 3 | Derivatives | `notebooks/03_derivatives.ipynb` |
| 4 | Derivative rules | `notebooks/04_derivative_rules.ipynb` |
| 5 | Antiderivatives | `notebooks/05_antiderivatives.ipynb` |
| 6 | Definite integrals | `notebooks/06_definite_integrals.ipynb` |
| 7 | Differential equations | `notebooks/07_differential_equations.ipynb` |

## Suggested setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
jupyter lab
```

Run Jupyter from the project root so the notebooks can import `calculus_lab` from `src/`.

## Run with Docker

Docker packages the Python version and course dependencies so the notebooks behave consistently across computers. From the project root:

```bash
docker compose up --build
```

Then open [http://localhost:8888](http://localhost:8888) and enter the token `calculus` when prompted. The project directory is mounted into the container, so notebook changes remain on your computer.

Stop the environment with `Ctrl+C`, or run:

```bash
docker compose down
```

The Docker image includes the dependencies and the shared `calculus_lab` package. It does not include your host machine's Python environment.

## Learning workflow

For each module, we will build the notebook in this order:

1. Intuition and visual exploration with NumPy and Plotly.
2. Exact symbolic work with SymPy.
3. Short explanations and worked examples.
4. Guided exercises, numerical checks, and a mini-project.
5. A checkpoint that connects the module to the next one.

The notebooks are intentionally scaffolded first. We will develop them module by module, starting with Module 1.
