import json,os
from datetime import datetime
from .Task import Task
class Tools:
    def __init__(self,filename=None):
        if filename is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.filename = os.path.join(base_dir, "tasks.json")
        else:
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
        new_task = Task(1, description)
        self.tasks.insert(0, new_task)
        for index, task in enumerate(self.tasks, start=1):
            task.id = index
        print("User Added Succeful !")
        self.save()
        print(f"Task added successfully ! ")    
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
        #for task in self.tasks :
            #task.id = task_id - 1
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
    def mark(self,marked,id) :
        found_id = None
        for task in self.tasks :
            if task.id == id :
                found_id = task 
        if found_id is None :
            print(f"Error: Task with ID {id} not found.")
            return
        found_id.status = marked    
        self.save()
    def list(self):
        for task in self.tasks :
            print(task.to_dict())        
    def list_by_status(self,status) :
        status_found = 0
        for task in self.tasks :
            if task.status == status :
                status_found = 1
                print(task.to_dict())
        if status_found == 0 :
            print(f"There is 0 Tasks with {status} left.")