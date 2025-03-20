import inspect
import importlib

MODULE_CLASSES = [
    ("geoh5py.workspace", "Workspace"),
    ("geoh5py.groups", "Group"),
    ("geoh5py.objects", "BlockModel"),
    ("geoh5py.objects", "Curve"),
    ("geoh5py.objects", "Drillhole"),
    ("geoh5py.objects", "GeoImage"),
    ("geoh5py.objects", "Grid2D"),
    ("geoh5py.objects", "Points"),
    ("geoh5py.objects", "Surface"),
]


def extract_class_signatures(module_name: str, class_name: str):
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get the class.
    cls = getattr(module, class_name)

    # Get the class methods
    properties = [] # inspect.getmembers(cls, predicate=lambda q: not callable(q))
    methods = inspect.getmembers(cls, predicate=callable)

    # Extract the method signatures.
    signatures = {}
    for name, property_ in properties:
        if name.startswith("_"):
            continue
        signatures[name] = ""
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
