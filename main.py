import sys
from manager.Tools import Tools
from manager.Task import Task

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        print("Commands: add, update, delete")
        return

    command = sys.argv[1]
    manager = Tools()

    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Missing description. Usage: python main.py add \"<description>\"")
                return
            manager.add(sys.argv[2])

        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Usage: python main.py update <id> \"<new description>\"")
                return
            manager.update(int(sys.argv[2]), sys.argv[3])

        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Usage: python main.py delete <id>")
                return
            manager.delete(int(sys.argv[2]))

        else:
            print(f"Unknown command: {command}")

    except ValueError:
        print("Error: ID must be a number!")

if __name__ == "__main__":
    main()