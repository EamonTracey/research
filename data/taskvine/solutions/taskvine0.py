import ndcctools.taskvine as vine

manager = vine.Manager()

task = vine.Task("date > current_date")
current_date_vine_file = manager.declare_file("current_date")
task.add_output(current_date_vine_file, "current_date")
manager.submit(task)

manager.wait()
