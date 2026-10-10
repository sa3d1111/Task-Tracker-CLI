import sys
from manager.Tools import Tools
from manager.Task import Task

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [args]")
        print("Commands: add, update, delete")
        return

    command = sys.argv[1]
    manager = Tools()

    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Missing description. Usage: task-cli add \"<description>\"")
                return
            manager.add(sys.argv[2])

        elif command == "update":
            if len(sys.argv) < 4 or len(sys.argv) > 4:
                print("Error: Usage: task-cli update <id> \"<new description>\"")
                return
            manager.update(int(sys.argv[2]), sys.argv[3])

        elif command == "delete":
            if len(sys.argv) < 3 or len(sys.argv) > 3:
                print("Error: Usage: task-cli delete <id>")
                return
            manager.delete(int(sys.argv[2]))
        elif command == "mark-in-progress" :
            if len(sys.argv) < 2 or len(sys.argv) > 2 :
                print("Error: Usage: task-cli mark-in-progress <id>")
                return                    
            manager.mark("in-progress",int(sys.argv[2]))
        elif command == "mark-done" :
            if len(sys.argv) != 3  :
                print("Error: Usage: task-cli mark-done <id>")
                return                    
            manager.mark("done",int(sys.argv[2]))
        elif command == "list" :       
            if len(sys.argv) == 2   :
                manager.list()
                return
            if sys.argv[2] not in ["done","todo","in-progress"] :
                print(f"{sys.argv[2]} is not a status. ")
                return
            manager.list_by_status(sys.argv[2])                                
        else:
            print(f"Unknown command: {command}")
   
    except ValueError:
        print("Error: ID must be a number!")

if __name__ == "__main__":
    main()