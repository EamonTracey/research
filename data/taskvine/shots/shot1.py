# Prompt: Write a Python script that uses TaskVine to run the shell command
# hostname on a worker machine. The manager listens for workers on port 9123.
# The program waits for the task to be completed and prints a completion
# message before exiting.

import ndcctools.taskvine as vine

# Start the manager listening for workers on port 9123.
manager = vine.Manager(9123)

# Create a task that runs the hostname shell command.
task = vine.Task("hostname")

# Submit the task to the manager. An external worker may complete this task.
manager.submit(task)

# Loop while the manager has remaining tasks to be completed.
while not manager.empty():
    # Wait for task completion with a 5 second timeout.
    task = manager.wait(5)

    # If we have a completed task, print a completion message.
    if task is not None:
        print(f"Task {task.id} completed.")
