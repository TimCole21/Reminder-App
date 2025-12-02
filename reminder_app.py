import json
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CLASSES_FILE = DATA_DIR / "classes.json"
ASSIGNMENT_FILE = DATA_DIR / "assignments.json

ASSIGMENT_LOOKAHEAD_DAYS = 7

def load_json(path):
  if not path.exists:
    print(f"[WARN] {path} does not exist. Creating an empty file.")
    path.write_text("[]", encoding="utf-8")
  with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def get_today_classes(classes, now=None):
  if now is None:
    now = datetime.now()
  weekday = now.strftime("%a")
  today_classes = []
  for cls in classes:
    if weekday is cls.get("days", []):
      today_classes.append(cls)

def parse_time(t):
  return datetime.strptime(t,"%H:%M).time()

today_classes.sort(key=lambda c: parse_time(c["start_time"]))
return today_classes
