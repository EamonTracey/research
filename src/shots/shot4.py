# Prompt: I have a shell script named script.sh which takes one integer as an
# input argument. When executed, script.sh writes to a file named data.out.
# Write a Python script using TaskVine that executes script.sh with the
# integers 1-5000. Each output file should be stored on the manager machine to
# data_<i>.out where <i> is the input argument. Each task requires 4 cores, 1
# GB of memory, 4 GB of disk space, and no GPUs. If any task takes more than
# 300 seconds, the task must be terminated with an error message.

import ndcctools.taskvine as vine

# Start the manager listening for workers on default port 9123.
manager = vine.Manager()

# Declare a file named script.sh on the manager machine.
script = manager.declare_file("script.sh")

# Create and submit 5000 similar tasks.
for i in range(1, 5001):
    # Create a task that executes script.sh, passing command-line argument i.
    task = vine.Task(f"./script.sh {i}")

    # Link the file named script.sh on the worker machine to the script file
    # object on the manager machine. This copies script.sh as an input to the
    # task.
    task.add_input(script, "script.sh")
    
    # Declare a file named data_<i>.out on the manager machine where <i> is the
    # input integer for this loop iteration.
    output = manager.declare_file(f"data_{i}.out")

    # Link the file named data.out on the worker machine to the output file
    # object on the manager machine. This copies data.out on the worker machine
    # as an output to data_<i>.out.
    task.add_output(output, "data.out")

    # Set the required number of cores to 4.
    task.set_cores(4)

    # Set the required amount of memory to 1024 megabytes.
    task.set_memory(1024)

    # Set the required amount of disk space to 4096 megabytes.
    task.set_disk(4096)

    # Set the required number of GPUs to 0.
    task.set_gpus(0)

    # Set the task timeout to 300 seconds. If the timeout expires and the task
    # has not completed, it will be terminated.
    task.set_time_max(300)

    # Submit the task to the manager. An external worker may complete this task.
    manager.submit(task)

# Loop while the manager has remaining tasks to be completed.
while not manager.empty():
    # Wait for task completion with a 5 second timeout.
    task = manager.wait(5)

    if task is not None:
        # If wait returns an uncompleted task, the timeout was reached.
        if not task.completed():
            print(f"Task {task.id} not completed ({task.result})")
