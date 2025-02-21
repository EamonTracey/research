import ndcctools.taskvine as vine

manager = vine.Manager()
manager.enable_monitoring(watchdog=False)
manager.set_category_resources_min("intensive", {"cores": 8, "memory": 16 * 1024,})
manager.set_category_resources_min("light", {"cores": 1, "memory": 2 * 1024,})

intensive_vine_file = manager.declare_file("intensive.sh")
for _ in range(10):
    task = vine.Task("./intensive.sh")
    task.add_input(intensive_vine_file, "intensive.sh")
    task.set_category("intensive")
    manager.submit(task)

light_vine_file = manager.declare_file("light.sh")
for _ in range(100):
    task = vine.Task("./light.sh")
    task.add_input(light_vine_file, "light.sh")
    task.set_category("light")
    manager.submit(task)

while not manager.empty():
    task = manager.wait()
    print(task.std_output)
