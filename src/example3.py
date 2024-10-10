import ndcctools.taskvine as vine

manager = vine.Manager(5678)
names = manager.declare_file("names.txt")

for _ in range(100):
    task = vine.Task("shuf -n 1 file")
    task.add_input(names, "file")
    manager.submit(task)

while not manager.empty():
    task = manager.wait(1)
    if task is not None:
        print(f"id={task.id} host={task.hostname} exitcode={task.exit_code} result={task.result}")
        print(task.std_output)
