class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        self.tasks.append({"title": title, "done": False})


if __name__ == "__main__":
    todo = TaskList()
    todo.add("Buy milk")
    print(todo.tasks)
