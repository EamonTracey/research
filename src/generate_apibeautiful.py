import json

from bs4 import BeautifulSoup
import requests


URLS = {
        "ndcctools.taskvine.manager.Manager": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1manager_1_1Manager.html",
        #"ndcctools.taskvine.task.Task": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1Task.html",
        #"ndcctools.taskvine.task.LibraryTask": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1LibraryTask.html",
        #"ndcctools.taskvine.task.PythonTask": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1PythonTask.html",
        #"ndcctools.taskvine.task.FunctionCall": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1FunctionCall.html",
}

for name, url in URLS.items():
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    methods = []
    for memitem in soup.find_all("div", class_="memitem"):
        memname = memitem.find("td", class_="memname")
        if memname:
            # Extract the method.
            method_signature = memname.text.strip()
            method_name = method_signature.split("(")[0].split(".")[-1]  # Extract the method name
            
            # Extract the description.
            memdoc = memitem.find("div", class_="memdoc")
            description = memdoc.p.text.strip() if memdoc and memdoc.p else ""

            # Extract the parameters.
            parameters = []

            methods.append({
                "name": method_name,
                "description": description,
                "parameters": parameters
            })

    methods = json.dumps(methods, indent=4)
    print(methods)
