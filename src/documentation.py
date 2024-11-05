import inspect
import importlib


def extract_class_signatures(module_name: str, class_name: str):
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get the class.
    cls = getattr(module, class_name)

    # Get the class methods
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)

    # Extract the method signatures.
    signatures = {}
    for name, method in methods:
        if name.startswith("_") and name != "__init__":
            continue

        signature = inspect.signature(method)
        signatures[name] = str(signature)

    return signatures


manager_signatures = extract_class_signatures("ndcctools.taskvine.manager",
                                              "Manager")
task_signatures = extract_class_signatures("ndcctools.taskvine.task", "Task")

print("ndcctools.taskvine.manager.Manager")
for name, signature in manager_signatures.items():
    print(f"    {name}{signature}")

print("ndcctools.taskvine.manager.Manager")
for name, signature in manager_signatures.items():
    print(f"    {name}{signature}")
