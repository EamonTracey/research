import inspect
import importlib

MODULE_CLASSES = [
    ("ndcctools.taskvine.manager", "Manager"),
    ("ndcctools.taskvine.task", "Task"),
    ("ndcctools.taskvine.task", "LibraryTask"),
    ("ndcctools.taskvine.task", "PythonTask"),
    ("ndcctools.taskvine.task", "FunctionCall"),
    ("ndcctools.taskvine.futures", "FuturesExecutor"),
    ("ndcctools.taskvine.futures", "VineFuture"),
    ("ndcctools.taskvine.futures", "FuturePythonTask"),
    ("ndcctools.taskvine.futures", "FutureFunctionCall"),
]


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


def main():
    for module, class_ in MODULE_CLASSES:
        signatures = extract_class_signatures(module, class_)

        print(f"{module}.{class_}")
        for name, signature in signatures.items():
            print(f"    {name}{signature}")


if __name__ == "__main__":
    main()
