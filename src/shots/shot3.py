# Prompt: I have a file names.txt that contains one first name per line. Write
# a Python script using TaskVine that launches 100 tasks. Each task prints a
# random name. Wait for all tasks to be completed. Upon completion of a task,
# the script should print task metadata, including the id, hostname, exit code,
# and result. Also, print each task's stdout. The manager runs on port 5678.

import ndcctools.taskvine as vine

# Start the manager listening for workers on port 5678.
manager = vine.Manager(5678)

# Declare a file named names.txt on the manager machine.
names = manager.declare_file("names.txt")

# Create and submit 100 identical tasks.
for _ in range(100):
    # Create a task that runs the shuf shell command to print 1 random line
    # from the file named file.
    task = vine.Task("shuf -n 1 file")

    # Link the file named file on the worker machine to the names file object
    # on the manager machine. This copies names.txt as an input to the task.
    task.add_input(names, "file")

    # Submit the task to the manager. An external worker may complete this task.
    manager.submit(task)

# Loop while the manager has remaining tasks to be completed.
while not manager.empty():
    # Wait for task completion with a 1 second timeout.
    task = manager.wait(1)

    if task is not None:
        # Print a completion message with task metadata.
        print(f"id={task.id} host={task.hostname} "
              f"exitcode={task.exit_code} result={task.result}")

        # Print the stdout of the task.
        print(task.std_output)
