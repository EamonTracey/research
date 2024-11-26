import os

import ndcctools.taskvine as vine

os.makedirs("script_outputs", exist_ok=True)

manager = vine.Manager()

script_vine_file = manager.declare_file("script.sh")
file1_vine_file = manager.declare_file("script_inputs/file1.input")
file2_vine_file = manager.declare_file("script_inputs/file2.input")
for i in range(1, 1001):
    task = vine.Task(f"./script.sh {i} file1.input file2.input")
    task.add_input(script_vine_file, "script.sh")
    task.add_input(file1_vine_file, "file1.input")
    task.add_input(file2_vine_file, "file2.input")
    output_vine_file = manager.declare_file(f"script_outputs/output{i}.txt")
    task.add_output(output_vine_file, f"output{i}.txt")
    manager.submit(task)

while not manager.empty():
    manager.wait()
