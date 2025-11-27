# Day 02 – Calculator + Text Playground (Modules & Packages)

Finally got a proper grip on how real Python projects are organized!  
No more dumping everything in one file.

### What I built & learned
- Turned `utils/` into a real package using `__init__.py`
- Split code into separate modules: `math_ops.py`, `string_ops.py`, `validators.py`
- Clean imports in `main.py` → `from utils import add, is_number, ...`
- Added `if __name__ == "__main__":` guards in every module
- Wrote docstrings everywhere (feels so professional now)
- Bonus: saves results to `output.txt`

### Resources that actually helped
- Corey Schafer – Modules and Packages → https://www.youtube.com/watch?v=0gx3n2F5i1w
- ArjanCodes – Project Structure → https://www.youtube.com/watch?v=xVuqDBCQAYc
- Quick __init__.py explanation → https://www.youtube.com/watch?v=VEbuZox5qC4