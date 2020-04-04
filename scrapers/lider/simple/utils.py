import os, copy, json, csv, datetime
from pathlib import Path

def save_into_csv(information):
  project_folder_path = Path().absolute()
  file_location = '{}/output/lider/simple/lidersimple_{}.csv'.format(project_folder_path, str(datetime.datetime.now()))
  os.makedirs(os.path.dirname(file_location), exist_ok = True)
  csv_file = open(file_location, 'w')
  with csv_file:
    columns = ['Producto', 'Sku', 'Precio', 'Unidad/Medida']
    writer = csv.DictWriter(csv_file, fieldnames = columns)    
    writer.writeheader()
    for i in information:
      writer.writerow({
        'Producto': i.name,
        'Sku': i.sku,
        'Precio': i.price,
        'Unidad/Medida': i.measure
      })