import ndcctools.taskvine as vine

manager = vine.Manager()

task = vine.Task("./train_demo")
binary_vine_file = manager.declare_file("train_demo")
task.add_input(binary_vine_file, "train_demo")
model_vine_file = manager.declare_file("model.tar.gz")
task.add_output(model_vine_file, "model.tar.gz")
task.add_feature("NVIDIA RTX 4090")
manager.submit(task)

manager.wait()
