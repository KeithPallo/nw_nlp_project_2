import json

with open('veggiecooking.json', 'r') as f:
    data = json.load(f)

print(data)
