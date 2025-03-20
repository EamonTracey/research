import json

from bs4 import BeautifulSoup
import requests

URLS = {
        "geoh5py.workspace": "https://mirageoscience-geoh5py.readthedocs-hosted.com/en/stable/content/api/geoh5py.workspace.html",
        "geoh5py.groups": "https://mirageoscience-geoh5py.readthedocs-hosted.com/en/stable/content/api/geoh5py.groups.html",
        "geoh5py.objects": "https://mirageoscience-geoh5py.readthedocs-hosted.com/en/stable/content/api/geoh5py.objects.html"
}
CLASSES = [
    "Workspace",
    "Group",
    "BlockModel",
    "Curve",
    "Drillhole",
    "GeoImage",
    "Grid2D",
    "Points",
    "Surface",
]


for name, url in URLS.items():
    html = requests.get(url).text
    soup_ = BeautifulSoup(html, "html.parser")
    print(f"{name}")

    for soup in soup_.find_all("dl", class_="py class"):
        dt = soup.find("dt", class_="sig sig-object py")
        class_name = dt.find("span", class_="sig-prename").text.strip() + dt.find("span", class_="sig-name").text.strip()
        if class_name.split(".")[-1] not in CLASSES:
            continue
        params = ", ".join(em.text.strip() for em in dt.find_all("em", class_="sig-param"))
        print(f" {class_name}({params})")

        attributes = []
    #    for _ in []:
    #        attributes.append({
    #            "name": "",
    #            "description": "",
    #        })

        methods = []
        for dl in soup.find_all("dl", class_="py method"):
            name_tag = dl.select_one("span.pre")
            method_name = name_tag.get_text(strip=True) if name_tag else None

            description_tag = dl.select_one("dd p")
            description = description_tag.get_text(strip=True) if description_tag else ""

            parameters = []
            for li in dl.select(".field-list ul li"):
                param_name = li.find("strong").text.strip()
                description = li.get_text(strip=True).split("–", 1)[-1].strip()
                parameters.append({"name": param_name, "description": description})
                
            methods.append({
                "name": method_name,
                "description": description,
                "parameters": parameters
            })


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
                    print(f"   {parameter['name']} - {parameter['description']}")
