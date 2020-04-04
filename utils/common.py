import json
from pathlib import Path

def load_entries(path):
  with open(path) as file:
    entries = json.load(file)
  return entries['entries']

def get_configs():
  path = Path().absolute()
  with open(path) as file:
    configs = json.load(file)
  return configs