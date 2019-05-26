import os
import json
import datetime
import csv
from pathlib import Path
from entry_processor import process_entry

def load_urls():
  project_folder_path = Path().absolute()
  with open('{}/urls.json'.format(project_folder_path), 'r') as file:
    urls = json.load(file)
  return urls['entries']

def process_entries(entries):
  result = list()
  for entry in entries:
    information = process_entry(entry)
    result.extend(information)
  return result

def save_into_csv(information):
  project_folder_path = Path().absolute()
  file_location = '{}/output/result_{}.csv'.format(project_folder_path, str(datetime.datetime.now()))
  os.makedirs(os.path.dirname(file_location), exist_ok=True)
  csv_file = open(file_location, 'w')
  with csv_file:
    columns = ['Producto', 'Precio Regular', 'Precio Actual', 'Unidad/Medida', 'Promociones', 'Validez Promociones']
    writer = csv.DictWriter(csv_file, fieldnames = columns)    
    writer.writeheader()
    for i in information:
      writer.writerow({
        'Producto': i.name,
        'Precio Regular': i.regular_price,
        'Precio Actual': i.current_price,
        'Unidad/Medida': i.measure,
        'Promociones': i.promotions,
        'Validez Promociones': i.promotions_period
      })