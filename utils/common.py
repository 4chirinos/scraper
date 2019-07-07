import json
from pathlib import Path

def load_entries(path):
  project_folder_path = Path().absolute()
  with open('{}/{}'.format(project_folder_path, path), 'r') as file:
    entries = json.load(file)
  return entries['entries']