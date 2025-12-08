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

def get_upcoming_assignments(assignments, now=None, days_ahead=7):
  if now is None:
    now = datetime.now()
  upcoming = []
  end = now + timedelta(days=days_ahead)
  
  for a in assignments:
    if a.get("status","pending") != "pending":
      continue
    
    due_str = a.get("due")
    if not due_str:
      continue

  try:
    due_dt = datetime.strptime(due_str,"%Y-%m-%d %H:%M")
  except ValueError:
    print(f"[WARn} Bad date format for assignment: {a}")
    continue

def print_today_classes(today_classes, now=None):
  if now is None:
    now = datetime.now()

  print("===Today's Classes===")
  if not today_classes:
    print("No classes today")
    return
  for cls in today_classes:
    name = cls.get("name")
    code = cls.get("code", "")
    start = cls.get("start_time")
    end = cls.get("end_time")
    location = cls.get("location", "TBA")

    print(f"- {start}-{end} | {code} {name} @{location}")

def print_upcoming_assignments(upcoming_assigments, now=None, days_ahead=7):
  if now is None:
    now = datetime.now()
  print(f"\n=== Assignments Due in Next {days_ahead} Days===")
  if not upcoming_assignments:
    print("Everything is completed")
    return

  for a in upcoming_assignments:
    title = a.get("title")
    course = a.get("course", "")
    due_dt = a["_due_dt"]
    days_left = (due_dt.date() - now.date()).days

    when_str = due_dt.strftime("%Y-%m-%d %H:%M")
    if days_left ==0:
      rel = "TODAY"
    elif days_left ==1:
      rel = "tomorrow"
    else:
      rel = f"in {days_left} days"

    print(f"- [{course}] {title} -> {when_str} ({re;})")

def main():
  print("Student Reminder App\n")

  classes = load_json(CLASSES_FILE)
  assignments = load_json(ASSIGNMENTS_FILE)

  now = datetime.now()

  today_classes = get_today_classes(classes, now=now)
  upcoming_assignments = get_upcoming_assignments(assignments, now=now, days_ahead=ASSIGNMENT_LOOKAHEAD_DAYS)

  print_today_classes(today_classes, now=now)
  print_upcoming_assignments(upcoming_assignments, now=now, days_ahead=ASSIGNMENT_LOOKAHEAD_DAYS)

if __name__ == "__main__":
  main()
  
                               
