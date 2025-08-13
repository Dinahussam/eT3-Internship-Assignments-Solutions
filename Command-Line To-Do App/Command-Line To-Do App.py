import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

db_path = Path("tasks.json")


def load_tasks():
    if db_path.exists():
        return json.loads(db_path.read_text())
    return []


def save_tasks(tasks):
    db_path.write_text(json.dumps(tasks, indent=2))


while True:
    cmd = input("Command (add/list/done/delete/exit): ").strip().lower()
    tasks = load_tasks()

    if cmd == "add":
        text = input("Task: ")
        priority = input("Priority (optional): ") or None
        tags_str = input("Tags (comma separated, optional): ")
        tags = tags_str.split(",") if tags_str else []
        task = {
            "id": len(tasks) + 1,
            "text": text,
            "done": False,
            "priority": priority,
            "tags": [t.strip() for t in tags if t.strip()],
            "created_at": datetime.now(ZoneInfo("Africa/Cairo")).strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")

    elif cmd == "list":
        for t in tasks:
            status = "✓" if t["done"] else " "
            print(f"{t['id']}. [{status}] {t['text']} (priority={t['priority']}, tags={t['tags']}, createdAt={t['created_at']})")

    elif cmd == "done":
        tid = int(input("Task ID to mark done: "))
        for t in tasks:
            if t["id"] == tid:
                t["done"] = True
        save_tasks(tasks)

    elif cmd == "delete":
        tid = int(input("Task ID to delete: "))
        tasks = [t for t in tasks if t["id"] != tid]
        for index, task in enumerate(tasks, start=1):
            task["id"] = index
        save_tasks(tasks)

    elif cmd == "exit":
        break

    else:
        print("Unknown command.")