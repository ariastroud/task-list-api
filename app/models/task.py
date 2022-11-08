from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    @classmethod
    def from_dict(cls, data_dict):
        return cls(title=data_dict["title"], description=data_dict["description"])

    def to_dict(self):
        completed = None
        if not self.completed_at:
            completed = False
        else:
            completed = True 
        
        # if goal id return
        if self.goal_id:
            return {
                    "id": self.task_id,
                    "goal_id": self.goal_id,
                    "title": self.title,
                    "description": self.description,
                    "is_complete": completed
                }
        else:
            return {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": completed
            }

    # def to_dict_one(self):
    #     completed = None
    #     if not self.completed_at:
    #         completed = False
    #     else:
    #         completed = True 
    #     return {
    #         "task": {
    #             "id": self.task_id,
    #             "title": self.title,
    #             "description": self.description,
    #             "is_complete": completed }
    #         }