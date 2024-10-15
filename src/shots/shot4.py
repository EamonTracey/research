import ndcctools.taskvine as vine

manager = vine.Manager()
script = manager.declare_file("script.sh")

for i in range(1, 5001):
    task = vine.Task(f"./script.sh {i}")

    task.add_input(script, "script.sh")
    
    output = manager.declare_file(f"data_{i}.out")
    task.add_output(output, "data.out")

    task.set_cores(4)
    task.set_memory(1024)
    task.set_disk(4096)
    task.set_gpus(0)
    task.set_time_max(300)

    manager.submit(task)

while not manager.empty():
    task = manager.wait(5)
    if task is not None:
        if not task.completed():
            print(f"Task {task.id} not completed ({task.result})")
