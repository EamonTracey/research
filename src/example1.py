import ndcctools.taskvine as vine

manager = vine.Manager(9123)

task = vine.Task("hostname")
manager.submit(task)

while not manager.empty():
    task = manager.wait(5)
    if task is not None:
        print(f"Task {task.id} completed.")
