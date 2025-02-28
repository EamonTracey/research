import json

from bs4 import BeautifulSoup
import requests

URLS = {
    "airtrafficsim.core.environment.Environment": "https://hkust-octad-lab.github.io/AirTrafficSim/api/core/airtrafficsim.core.environment.html",
    "airtrafficsim.core.aircraft.Aircraft": "https://hkust-octad-lab.github.io/AirTrafficSim/api/core/airtrafficsim.core.aircraft.html",
    "airtrafficsim.core.traffic.Traffic": "https://hkust-octad-lab.github.io/AirTrafficSim/api/core/airtrafficsim.core.traffic.html#airtrafficsim.core.traffic.Traffic",
}

for name, url in URLS.items():
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    attributes = []
    for dl in soup.select("dl.py.attribute"):
        name_tag = dl.select_one(".sig-name .pre")
        method_name = name_tag.get_text(strip=True) if name_tag else None

        description_tag = dl.select_one("dd p")
        description = description_tag.get_text(strip=True) if description_tag else None

        attributes.append({
            "name": method_name,
            "description": description,
        })

    methods = []
    for dl in soup.select("dl.py.method"):
        name_tag = dl.select_one(".sig-name .pre")
        method_name = name_tag.get_text(strip=True) if name_tag else None

        description_tag = dl.select_one("dd p")
        description = description_tag.get_text(strip=True) if description_tag else None

        param_tags = dl.select(".sig-param")
        parameters = []
        for param in param_tags:
            param_name = param.get_text(strip=True)
            param_desc_tag = dl.select_one(f"dt:has(strong:contains('{param_name}')) + dd p")
            param_description = param_desc_tag.get_text(strip=True) if param_desc_tag else ""
            parameters.append({"name": param_name, "description": param_description})

        methods.append({
            "name": method_name,
            "description": description,
            "parameters": parameters
        })

    print(name)
    for attribute in attributes:
        attribute["description"] = attribute["description"].replace("\n", " ")
        print(
            f"  {attribute['name']} - {attribute['description']}"
        )

    for method in methods:
        method["description"] = method["description"].replace("\n", " ")
        print(
            f"  {method['name']}({', '.join([p['name'] for p in method['parameters']])}) - {method['description']}"
        )
        for parameter in method["parameters"]:
            parameter["description"] = parameter["description"].replace(
                "\n", " ")
            if parameter["description"]:
                print(f"    {parameter['name']} - {parameter['description']}")
