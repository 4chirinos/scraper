import os
import json
import datetime
import csv
from pathlib import Path

def load_entries():
  project_folder_path = Path().absolute()
  with open('{}/lider/entries.json'.format(project_folder_path), 'r') as file:
    entries = json.load(file)
  return entries['entries']