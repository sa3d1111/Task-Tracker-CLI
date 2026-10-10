# 📝 Task Tracker CLI

A lightweight, robust Command-Line Interface (CLI) application built with Python to manage daily tasks, featuring local JSON persistence and portable execution.

---

## ✨ Features

- **CLI-Native Execution**: Run commands seamlessly via `task-cli` from any directory.
- **Full CRUD Management**: Add, update, delete, and list tasks directly from the terminal.
- **Status Lifecycle**: Toggle progress states between `todo`, `in-progress`, and `done`.
- **Dynamic Filtering**: Filter stored tasks by their current status.
- **Smart ID Re-indexing**: Automatically assigns ID `1` to new tasks and dynamically re-sequences remaining tasks upon deletion.
- **Zero External Dependencies**: Built strictly using the Python standard library.

---

## 📁 Project Architecture

```text
task-tracker/
│
├── manager/
│   ├── __init__.py      # Package marker
│   ├── Task.py          # Data model, ISO timestamps & serialization
│   └── Tools.py         # Business logic & persistent storage engine
│
├── tasks.json           # Local JSON database
├── main.py              # CLI entry point & argument parsing
├── setup.py             # Packaging configuration for portable CLI
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/sa3d1111/Task-Tracker-CLI.git](https://github.com/sa3d1111/Task-Tracker-CLI.git)
cd task-tracker
```

### 2. Install as a Portable CLI (Recommended)
Install the package in editable mode using `pip`:

```bash
pip install -e .
```

*Note: If `pip` is not in your system PATH, use:*
```bash
python -m pip install -e .
```

Once installed, you can execute commands globally using `task-cli` instead of `python main.py`.

---

## 💻 Usage & Commands

### Add a Task
Adds a new task with status `todo` and assigns it as ID `1` (shifting existing tasks down):
```bash
task-cli add "Buy groceries"
```

### Update a Task
Update the description of an existing task by its ID:
```bash
task-cli update 1 "Buy groceries and make dinner"
```

### Delete a Task
Delete a task by ID (remaining task IDs are automatically re-indexed):
```bash
task-cli delete 1
```

### Mark Status
Update progress state:
```bash
# Mark as in-progress
task-cli mark-in-progress 1

# Mark as done
task-cli mark-done 1
```

### List Tasks
View all tasks or filter by state:
```bash
# View all tasks
task-cli list

# Filter by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

---

## 📋 Data Schema (`tasks.json`)

Data is persisted locally in JSON format with structured ISO 8601 timestamps:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-10-10T14:39:00",
    "updatedAt": "2026-10-10T14:39:00"
  }
]
```

---

## 👤 Author

- **Saad BENBAHI** - Applied Informatics Student
- GitHub: [@sa3d1111](https://github.com/sa3d1111)