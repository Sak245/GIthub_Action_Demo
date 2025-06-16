### ✅ Python Maths Operation Demo with GitHub Actions

This project demonstrates:

* A simple Python module with `add` and `sub` operations
* Unit tests using `pytest`
* Automated testing with **GitHub Actions**

---

### 📁 Project Structure

```
.
├── src/
│   └── maths_operation.py       # Contains add and sub functions
├── tests/
│   └── test_operations.py       # Pytest unit tests
├── requirements.txt             # Python dependencies (e.g., pytest, pandas)
├── .github/
│   └── workflows/
│       └── unitest.yml          # GitHub Actions workflow
├── README.md                    # You're here!
```

---

### 📦 Requirements

```
pytest
pandas
```

Install them locally with:

```bash
pip install -r requirements.txt
```

---

### 🚀 Run Tests Locally

```bash
pytest
```

---

### 🤖 GitHub Actions Workflow

This project uses [GitHub Actions](https://github.com/features/actions) to:

* Install Python 3.10
* Lint code using `flake8`
* Run tests using `pytest`

Workflow file: `.github/workflows/unitest.yml`

On every **push** or **pull request** to the `main` branch, the pipeline automatically runs and shows pass/fail status.
