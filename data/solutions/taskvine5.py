import ndcctools.taskvine as vine

manager = vine.Manager()
manager.enable_monitoring(watchdog=False)
manager.set_category_resources_max("category", {"cores": 4, "memory": 1024, "disk": 2048})

command = """cd complex_project
make all
make test
"""
task = vine.Task(command)
project_vine_directory = manager.declare_file("complex_project")
task.add_input(project_vine_directory, "complex_project")
task.set_category("category")
manager.submit(task)

task = manager.wait()
print(task.exit_code)
print(task.std_output)
if task.limits_exceeded and task.limits_exceeded.cores > -1:
    print(f"Overused cores: {task.resources_measured.cores - task.resources_allocated.cores}")
if task.limits_exceeded and task.limits_exceeded.memory > -1:
    print(f"Overused memory: {task.resources_measured.memory - task.resources_allocated.memory}")
if task.limits_exceeded and task.limits_exceeded.disk > -1:
    print(f"Overused disk: {task.resources_measured.disk - task.resources_allocated.disk}")
