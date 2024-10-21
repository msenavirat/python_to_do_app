class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_done(self):
        self.completed = True

    def mark_undone(self):
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} [{status}]"
 