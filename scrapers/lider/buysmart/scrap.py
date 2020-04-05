import logging, json, copy
import configparser
from pathlib import Path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from .utils import save_into_csv
from ...utils import set_query_string_parameter_from_qs
from .extractors import extract_total_products, extract_products, extract_product_information

config = configparser.RawConfigParser()
config.read('{}/scraper.properties'.format(Path().absolute()))
LIDER_BUYSMART = dict(config.items('LIDER_BUYSMART'))

URL = LIDER_BUYSMART['url']

def scrap(entries):
  logging.info('Processing Líder buysmart')
  information = process_entries(entries)
  save_into_csv(information)
  print('Líder buysmart done...')
  logging.info('Ending Líder buysmart')

def prepare_payload(entry, n_products_to_retrieve):
  entry_copy = copy.deepcopy(entry)
  payload = entry_copy['requests'][0]
  params = payload['params']
  payload['params'] = set_query_string_parameter_from_qs(params, 'hitsPerPage', n_products_to_retrieve)
  entry_copy['requests'][0] = payload
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
  #print('Processing entry: {}'.format(entry))
  try:
    total_products = extract_total_products(get_data(entry, 1))
    products = extract_products(get_data(entry, total_products))
    for product in products:
      product_information = extract_product_information(product)
      result.append(product_information)
  except Exception as e:
    logging.error('Failure processing: {}'.format(entry))
    logging.error(e)
  return result