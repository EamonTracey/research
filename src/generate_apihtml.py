import requests

URLS = {
    "ndcctools.taskvine.manager.Manager":
    "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1manager_1_1Manager.html",
    "ndcctools.taskvine.task.Task":
    "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1Task.html",
    #"ndcctools.taskvine.task.LibraryTask": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1LibraryTask.html",
    #"ndcctools.taskvine.task.PythonTask": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1PythonTask.html",
    #"ndcctools.taskvine.task.FunctionCall": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1FunctionCall.html",
}


def main():
    for name, url in URLS.items():
        text = requests.get(url).text
        with open(name, "w") as fp:
            fp.write(text)


if __name__ == "__main__":
    main()
