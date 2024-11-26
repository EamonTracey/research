import requests

URLS = {
        "ndcctools.taskvine.manager.Manager": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1manager_1_1Manager.html",
#        "": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1Task.html",
#        "": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1LibraryTask.html",
#        "": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1PythonTask.html",
#        "": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1FunctionCall.html",
}


def main():
    for name, url in URLS.items():
        text = requests.get(url).text
        with open(name, "w") as fp:
            fp.write(text)


if __name__ == "__main__":
    main()
