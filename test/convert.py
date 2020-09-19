import json

with open('reference.json') as f:
  ref = json.load(f)

print(ref)