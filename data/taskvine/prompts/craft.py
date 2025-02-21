import json

j = json.load(open("taskvine_prompts.json"))

#manager_reference = open("ndcctools.taskvine.manager.Manager").read()
#j["system"] = []
#j["system"].append("You are a helpful TaskVine coding assistant. Provide strictly the requested code using the ndcctools.taskvine library.")
#j["system"].append(f"The first half of the detailed API reference site in HTML for ndcctools.taskvine.manager.Manager is below:\n{manager_reference[:len(manager_reference) // 2]}")
#j["system"].append(f"The second half of the detailed API reference site in HTML for ndcctools.taskvine.manager.Manager is below:\n{manager_reference[len(manager_reference) // 2:]}")

#manual = open("manual/manual").read()
#j["system"] = f"You are a helpful TaskVine coding assistant. Provide strictly the requested code using the ndcctools.taskvine library. The TaskVine user manual is below:\n{manual}"

#apihtml = open("apihtml/apihtml").read()
#j["system"] = f"You are a helpful TaskVine coding assistant. Provide strictly the requested code using the ndcctools.taskvine library. The TaskVine user manual is below:\n{apihtml}"

#apibeautiful = open("apibeautiful/apibeautiful").read()
#j["system"] = []
#j["system"].append("You are a helpful TaskVine coding assistant. Provide strictly the requested code using the ndcctools.taskvine library.")
#j["system"].append(f"The detailed API description of the ndcctools.taskvine library is below, including all classes, methods, and parameters with descriptions:\n{apibeautiful}")

manual = open("manual/manual").read()
apibeautiful = open("apibeautiful/apibeautiful").read()
j["system"] = []
j["system"].append("You are a helpful TaskVine coding assistant. Provide strictly the requested code using the ndcctools.taskvine library.")
j["system"].append(f"The TaskVine user manual is below:\n{manual}")
j["system"].append(f"The detailed API description of the ndcctools.taskvine library is below, including all classes, methods, and parameters with descriptions:\n{apibeautiful}")

#manual = open("manual/manual").read()
#apisum = open("apisum/apisum").read()
#j["system"] = []
#j["system"].append("You are a helpful TaskVine coding assistant. Provide strictly the requested code using the ndcctools.taskvine library.")
#j["system"].append(f"The TaskVine user manual is below:\n{manual}")
#j["system"].append(f"The simple API description of the ndcctools.taskvine library is below, including all classes, methods, and parameters:\n{apisum}")

with open("crafted.json", "w") as fp:
    json.dump(j, fp)
