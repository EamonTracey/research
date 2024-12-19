import json

from bs4 import BeautifulSoup
import requests


URLS = {
        "ndcctools.taskvine.manager.Manager": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1manager_1_1Manager.html",
        "ndcctools.taskvine.task.Task": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1Task.html",
        "ndcctools.taskvine.task.LibraryTask": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1LibraryTask.html",
        "ndcctools.taskvine.task.PythonTask": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1PythonTask.html",
        "ndcctools.taskvine.task.FunctionCall": "https://cctools.readthedocs.io/en/latest/api/html/classndcctools_1_1taskvine_1_1task_1_1FunctionCall.html",
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
            method_name = method_signature.split("(")[0].split(".")[-1]
            
            # Extract the description.
            memdoc = memitem.find("div", class_="memdoc")
            description = memdoc.p.text.strip() if memdoc and memdoc.p else ""

            # Extract the parameters.
            parameters = []
            params_section = memdoc.find("dl", class_="params")
            if params_section:
                for row in params_section.find_all("tr"):
                    param_name = row.find("td", class_="paramname").text.strip()
                    param_desc = row.find_all("td")[1].text.strip() if len(row.find_all("td")) > 1 else ""
                    parameters.append({"name": param_name, "description": param_desc})

            methods.append({
                "name": method_name,
                "description": description,
                "parameters": parameters
            })

    print(name)
    for method in methods:
        method["description"] = method["description"].replace("\n", " ")
        print(f"  {method['name']}({', '.join([p['name'] for p in method['parameters']])}) - {method['description']}")
        for parameter in method["parameters"]:
            parameter["description"] = parameter["description"].replace("\n", " ")
            print(f"    {parameter['name']} - {parameter['description']}")
