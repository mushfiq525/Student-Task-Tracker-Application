import json
import os
import random
from datetime import datetime
from task import Task

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()
    
    def generate_unique_id(self):
        existing = {t.task_id for t in self.tasks}
        while True:
            new_id = random.randint(1,1000)
            if new_id not in existing:
                return new_id
    
    def add_task(self, title, desctiption):
        try:
            task_id = self.generate_unique_id()
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task = Task(task_id, title, desctiption, created_at)
            self.tasks.append(task)
            print("Task added successfullt!")
        except Exception as e:
            print("Failed to add task:", e)
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n===== All tasks =====")
        for i, t in enumerate(self.tasks, start=1):
            print(f"{i}. Title: {t.title}")
            print(f"    Description: {t.description}")
            print(f"    Created At: {t.created_at}")
            print("---------------------")
        print()
    
    def find_task_index_by_id(self, task_id):
        for i, t in enumerate(self.tasks):
            if t.task_id == task_id:
                return i
        return None
    
    def update_tasks(self, task_id, new_title=None, new_description=None):
        try:
            idx = self.find_task_index_by_id(task_id)
            if idx is None:
                print(f"no task with ID {task_id} found.")
                return
            if new_title is not None and new_title.strip() != "":
                self.tasks[idx].title = new_title
            if new_description is not None and new_description.strip() != "":
                self.tasks[idx].description = new_description
            print("Task updated successfully!")
        except Exception as e:
            print("Failed to update task:", e)
    
    def delete_task(self, task_id):
        try:
            idx = self.find_task_index_by_id(task_id)
            if idx is None:
                print(f"no task with ID {task_id} found.")
                return
            removed = self.tasks.pop(idx)
            print(f"Task with ID {removed.task_id} deleted.")
        except Exception as e:
            print("Failed to delete task:", e)
    
    def save_to_file(self):
        try:
            data = [t.to_dict() for t in self.tasks]
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(json.dumps(data, indent=4))
        except Exception as e:
            print("Failed to save tasks to file:", e)
    
    def load_from_file(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    self.tasks = []
                    return
                data = json.loads(content)
                self.tasks = [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            print("Task file not found. Starting with empty list.")
            self.tasks = []
        except json.JSONDecodeError:
            print("Error reading tasks file. Starting with empty list.")
            self.tasks = []
        except Exception as e:
            print("An error occured while loading:", e)
            self.tasks = []