# Day 07 – File Handling & JSON Persistence

Today I made my bank system **permanent** – data survives even after closing the program!

### What I Learned Today
- Save bank data to a JSON file (`save_to_file`)
- Load data back when program starts (`load_from_file`)
- Handle errors like:
  - `FileNotFoundError` → no save file exists
  - `JSONDecodeError` → file is corrupted
- Convert dataclass to dictionary using `asdict()`

### Files
- `persistent_bank.py` → main code (Day 06 + save/load)
- `main.py` → test file (save → close → load again)
- `bank_data.json` → **automatically created** when you save
- `bank.log` → logs of all actions

### How to Run
```bash
python main.py