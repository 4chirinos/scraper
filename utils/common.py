import json

def load_entries(path):
  with open(path) as file:
    entries = json.load(file)
  return entries['entries']