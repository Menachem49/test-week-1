import json
from pathlib import Path

DB_FILE = Path(__file__).parent / "orderes.json"

def load_orderes():
    if not DB_FILE.exists():
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_orderes(orderes):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(orderes, file, indent=2, ensure_ascii=False)




