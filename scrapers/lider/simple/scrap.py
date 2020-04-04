import logging, json, copy
import configparser
from pathlib import Path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from .utils import save_into_csv
from .extractors import extract_products, extract_product_information

config = configparser.RawConfigParser()
config.read('{}/scraper.properties'.format(Path().absolute()))
LIDER_SIMPLE = dict(config.items('LIDER_SIMPLE'))

URL = LIDER_SIMPLE['url']
MAX_PRODUCTS = int(LIDER_SIMPLE['max_products'])

def scrap(entries):
  logging.info('Processing Líder simple')
  information = process_entries(entries)
  save_into_csv(information)
  print('Líder simple done...')
  logging.info('Ending Líder simple')

def prepare_payload(entry, n_products_to_retrieve):
  entry_copy = copy.deepcopy(entry)
  entry_copy['hitsPerPage'] = n_products_to_retrieve
  return entry_copy

def get_data(entry, n_products_to_retrieve):
  payload = prepare_payload(entry, n_products_to_retrieve)
  data = json.dumps(payload).encode('utf8')
  request = Request(URL, data = data, headers = {'User-Agent': 'Mozilla/5.0'})
  data = json.loads(urlopen(request).read().decode('utf8'))
  return data

def process_entries(entries):
  result = list()
  for entry in entries:
    information = process_entry(entry)
    result.extend(information)
  return result

def process_entry(entry):
  result = list()
  print('Processing entry: {}'.format(entry))
  try:
    total_products = MAX_PRODUCTS #extract_total_products(get_data(entry, 1))
    products = extract_products(get_data(entry, total_products))
    for product in products:
      product_information = extract_product_information(product)
      if product_information is not None:
        result.append(product_information)
  except Exception as e:
    logging.error('Failure processing: {}'.format(entry))
    logging.error(e)
  return result