 # Backend Engineering Journey 

## Day 01 - Modern Python + Virtual Environment (Completed Nov 17, 2025)

### What I Did Today
- Created isolated virtual environment (`venv`)
- Installed `requests` & `rich` libraries
- Used modern Python syntax:
  - Type hints
  - f-strings
  - Walrus operator
  - Rich pretty printing
- Wrote `setup_check.py` that:
  - Prints Python version
  - Imports libraries
  - Calculates factorial with type hints
  - Saves output to `output.txt`

### How to Run
```bash
cd day01
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
python setup_check.py
