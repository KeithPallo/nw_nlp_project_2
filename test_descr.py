import json

with open('descriptors_kb.json') as f:
	descriptors = json.load(f)

descriptors_list = []
for each in descriptors:
	descriptors_list.extend(descriptors[each])

print(descriptors_list.lower())