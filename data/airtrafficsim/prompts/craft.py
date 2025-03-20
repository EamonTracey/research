import json

j = json.load(open("airtrafficsim_prompts.json"))

apisum = open("../strategy/apisum/airtrafficsim_apisum.txt").read()
#j["system"] = [j["system"]]
#j["system"].append(f"The API reference is below:\n{apisum}")

apidocs = open("../strategy/apidocs/airtrafficsim_apidocs.txt").read()
#j["system"] = [j["system"]]
#j["system"].append(f"The API reference with documentation is below:\n{apidocs}")

manual = open("../strategy/manual/airtrafficsim_manual.txt").read()
#j["system"] = [j["system"]]
#j["system"].append(f"The AirTrafficSim manual is below:\n{manual}")

j["system"] = [j["system"]]
j["system"].append(f"The API reference with documentation is below:\n{apidocs}")
j["system"].append(f"The AirTrafficSim manual is below:\n{manual}")

with open("crafted.json", "w") as fp:
    json.dump(j, fp)
