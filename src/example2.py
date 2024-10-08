import ndcctools.taskvine as vine

manager = vine.Manager(9123)
output_file = manager.declare_file("output")

task = vine.Task("hostname > output")
task.add_output(output_file, "output")
manager.submit(task)

while not manager.empty():
    task = manager.wait(5)
    if task is not None:
        print(f"Task {task.id} completed.")
