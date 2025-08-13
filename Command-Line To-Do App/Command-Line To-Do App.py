import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

# Path to the JSON database file
db_path = Path("tasks.json")


def load_tasks():
    """
    Load tasks from the JSON file.

    Returns:
        list[dict]: List of task dictionaries.
    """
    if db_path.exists():
        return json.loads(db_path.read_text())
    return []


def save_tasks(tasks):
    """
    Save the given list of tasks to the JSON file.

    Args:
        tasks (list[dict]): List of task dictionaries to save.
    """
    db_path.write_text(json.dumps(tasks, indent=2))


def add_task():
    """
    Prompt the user for task details and add it to the task list.
    """
    tasks = load_tasks()
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


def list_tasks():
    """
    Display all tasks with their details.
    """
    tasks = load_tasks()
    for t in tasks:
        status = "✓" if t["done"] else " "
        print(f"{t['id']}. [{status}] {t['text']} (priority={t['priority']}, tags={t['tags']}, createdAt={t['created_at']})")


def mark_done():
    """
    Mark a specific task as completed.
    """
    tasks = load_tasks()
    tid = int(input("Task ID to mark done: "))
    for t in tasks:
        if t["id"] == tid:
            t["done"] = True
    save_tasks(tasks)


def delete_task():
    """
    Delete a specific task and reindex IDs.
    """
    tasks = load_tasks()
    tid = int(input("Task ID to delete: "))
    tasks = [t for t in tasks if t["id"] != tid]
    # Reindex task IDs
    for index, task in enumerate(tasks, start=1):
        task["id"] = index
    save_tasks(tasks)


def main():
    """
    Main loop for the task manager program.
    """
    while True:
        cmd = input("Command (add/list/done/delete/exit): ").strip().lower()
        tasks = load_tasks()

        if cmd == "add":
            add_task()

        elif cmd == "list":
            list_tasks()

        elif cmd == "done":
            mark_done()

        elif cmd == "delete":
            delete_task()

        elif cmd == "exit":
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()