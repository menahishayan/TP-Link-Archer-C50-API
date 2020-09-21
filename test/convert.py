import json

with open('test/reference.json') as f:
  ref = json.load(f)

print(ref)