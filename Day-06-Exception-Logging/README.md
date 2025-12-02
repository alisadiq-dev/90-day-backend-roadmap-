# Day 06 – Exception Handling + Logging

Today I made my bank system **super safe** and **professional**!

### What I Did Today
- Added custom errors (can't withdraw more than balance, can't deposit negative)
- Used `try/except` so the program never crashes
- Added **logging** – every action goes to `bank.log` file + shows on screen
- Success = INFO, Error = ERROR

### Files
- `bank_with_errors.py` → main code (Day 05 + errors + logging)
- `main.py` → test file
- `bank.log` → full record saved here
- `output.txt` → what you see on screen

### How to Run
```bash
python main.py