"""Simple terminal task manager."""
import argparse

TASKS = []

def add_task(desc):
    TASKS.append({"desc": desc, "done": False})

def list_tasks():
    for i, t in enumerate(TASKS, 1):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['desc']}")

def complete_task(num):
    try:
        TASKS[num-1]["done"] = True
    except IndexError:
        print("Invalid task number")

def main():
    parser = argparse.ArgumentParser(prog="taskmgr")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("add", help="Add a task").add_argument("desc")
    sub.add_parser("list", help="List tasks")
    sub.add_parser("done").add_argument("num", type=int)
    args = parser.parse_args()
    if args.cmd == "add":
        add_task(args.desc)
    elif args.cmd == "list":
        list_tasks()
    elif args.cmd == "done":
        complete_task(args.num)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()