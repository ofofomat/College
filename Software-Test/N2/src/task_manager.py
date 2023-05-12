class TaskManager:
    def __init__(self,):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        response = []
        for task in self.tasks:
            response.append(task.get_description())
        return response

    def mark_task_done(self, id):
        for task in self.tasks:
            if id is task.get_id():
                task.set_done()

    def remove_task(self, id):
        for task in self.tasks:
            if id is task.get_id():
                self.tasks.pop(id-1)
