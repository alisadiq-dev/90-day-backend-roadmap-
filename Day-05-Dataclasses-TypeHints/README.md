# Day 05 – Dataclasses & Type Hints

Aaj maine Day 4 wala Bank System ko modern banaya!

### Kya seekha?
- `@dataclass` → khud __init__ aur print bana deta hai
- Type hints → `amount: float`, `owner: str` likha
- `mypy` → code run se pehle galti pakad leta hai

### Files
- `typed_bank.py` → main code (dataclass + type hints)
- `main.py` → test karne ke liye
- `requirements.txt` → mypy install karne ke liye

### Kaise chalaye?
```bash
pip install mypy
python main.py           # for output run this command
mypy typed_bank.py      # for type check run this command