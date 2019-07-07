import os
import json
import datetime
import csv
from pathlib import Path

def load_entries():
  project_folder_path = Path().absolute()
  with open('{}/lider/supermarket/entries.json'.format(project_folder_path), 'r') as file:
    entries = json.load(file)
  return entries['entries']

def save_into_csv(information):
  project_folder_path = Path().absolute()
  file_location = '{}/lider/supermarket/output/result_{}.csv'.format(project_folder_path, str(datetime.datetime.now()))
  os.makedirs(os.path.dirname(file_location), exist_ok = True)
  csv_file = open(file_location, 'w')
  with csv_file:
    columns = ['Producto', 'Unidad/Medida', 'Precio Regular', 'Precio Actual', 'Precio por Unidad/Medida']
    writer = csv.DictWriter(csv_file, fieldnames = columns)    
    writer.writeheader()
    for i in information:
      writer.writerow({
        'Producto': i.name,
        'Unidad/Medida': i.measure,
        'Precio Regular': i.regular_price,
        'Precio Actual': i.current_price,
        'Precio por Unidad/Medida': i.price_measure_relation
      })