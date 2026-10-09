from datetime import datetime
class Task :
    def __init__(self,id,description,status="todo",createdAt=None,updatedAt=None):
        self.id = id
        self.description = description
        self.status = status
        now = datetime.now().isoformat(timespec="seconds")
        self.createdAt = createdAt if createdAt is not None else now
        self.updatedAt = updatedAt if updatedAt is not None else now
        
    def to_dict(self):
        return {
            "id" : self.id,
            "description" : self.description,
            "status" : self.status,
            "createdAt" : self.createdAt,
            "updatedAt" : self.updatedAt,
        }
    @classmethod
    def from_dict(cls,data):
        return cls(data["id"],data["description"],data["status"],data["createdAt"],data["updatedAt"])
    
    