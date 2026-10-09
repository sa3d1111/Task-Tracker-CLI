import json,os
from datetime import datetime
from manager.Task import Task
class Tools:
    def __init__(self,filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load()
    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as f :
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        else :
            pass        
    def save(self):
        with open(self.filename, "w") as f:
            json.dump([t.to_dict() for t in self.tasks],f,indent=4) 
    def add(self,description):
        new_id = max([t.id for t in self.tasks], default=0) + 1
        new_task = Task(new_id, description)
        print("User Added Succeful !")
        self.tasks.append(new_task)
        self.save()
        print(f"Task added successfully (ID: {new_id})")    
    def delete(self,task_id) :
        delete = None
        for task in self.tasks :
            if task.id == task_id :
                delete = task
                break
        if delete is None :
            print(f"Error: Task with ID {task_id} not found.")
            return
        self.tasks.remove(delete)
        for task in self.tasks :
            task.id = task_id - 1
        self.save()    
        print(f"Task {task_id} deleted successfully.")
    def update(self,id_dict,description):
        found_id = None
        for task in self.tasks :
            if task.id == id_dict :
                found_id = task 
        if found_id is None :
                print(f"Error: Task with ID {id_dict} not found.")
                return
        found_id.description = description
        found_id.updatedAt = datetime.now().isoformat(timespec="seconds")
        self.save()
        print(f"Task {id_dict} updates successfully.")     