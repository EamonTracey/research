import os

import ndcctools.taskvine as vine

manager = vine.Manager()

task = vine.Task("./script1.sh")
script1_vine_file = manager.declare_file("script1.sh")
task.add_input(script1_vine_file, "script1.sh")
intermediary_vine_file = manager.declare_temp()
task.add_output(intermediary_vine_file, "intermediary.out")
manager.submit(task)

task = vine.Task("./script2.sh intermediary.out")
script2_vine_file = manager.declare_file("script2.sh")
task.add_input(script2_vine_file, "script2.sh")
task.add_input(intermediary_vine_file, "intermediary.out")
output2_vine_file = manager.declare_file("script2.out")
task.add_output(output2_vine_file, "script2.out")
manager.submit(task)

task = vine.Task("./script3.sh intermediary.out")
script3_vine_file = manager.declare_file("script3.sh")
task.add_input(script3_vine_file, "script3.sh")
task.add_input(intermediary_vine_file, "intermediary.out")
output3_vine_file = manager.declare_file("script3.out")
task.add_output(output3_vine_file, "script3.out")
manager.submit(task)

while not manager.empty():
    manager.wait()
