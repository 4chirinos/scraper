import os, copy, json, csv, datetime
from pathlib import Path

def save_into_csv(information):
  project_folder_path = Path().absolute()
  file_location = '{}/output/lider/buysmart/result_{}.csv'.format(project_folder_path, str(datetime.datetime.now()))
  os.makedirs(os.path.dirname(file_location), exist_ok = True)
  csv_file = open(file_location, 'w')
  with csv_file:
    columns = ['Producto', 'Precio Regular', 'Precio Actual', 'Sku', 'Product Id']
    writer = csv.DictWriter(csv_file, fieldnames = columns)    
    writer.writeheader()
    for i in information:
      writer.writerow({
        'Producto': i.name,
        'Precio Regular': i.regular_price,
        'Precio Actual': i.current_price,
        'Sku': i.sku,
        'Product Id': i.id
      })

def prepare_payload(entry, n_products_to_retrieve):
  entry_copy = copy.deepcopy(entry)
  payload = entry_copy['requests'][0]
  params = payload['params']
  payload['params'] = params.format(n_products_to_retrieve)
  entry_copy['requests'][0] = payload
  return entry_copy