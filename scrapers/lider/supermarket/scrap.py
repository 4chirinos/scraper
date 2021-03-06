import logging
import configparser
from pathlib import Path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from .extractors import extract_products_information
from .utils import save_into_csv
from ...utils import set_query_string_parameter_from_url

config = configparser.RawConfigParser()
config.read('{}/scraper.properties'.format(Path().absolute()))
LIDER_SUPERMARKET = dict(config.items('LIDER_SUPERMARKET'))

MAX_PRODUCTS = int(LIDER_SUPERMARKET['max_products'])

def scrap(entries):
  print('Starting Líder supermarket')
  logging.info('Processing Líder supermarket')
  information = process_entries(entries)
  save_into_csv(information)
  print('Líder supermarket done...')
  logging.info('Ending Líder supermarket')

def process_entries(entries):
  result = list()
  for entry in entries:
    information = process_entry(entry)
    result.extend(information)
  return result

def process_entry(entry):
  result = list()
  url = set_query_string_parameter_from_url(entry, 'Nrpp', MAX_PRODUCTS)
  print('Processing: {}'.format(url))
  request = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
  try:
    response = urlopen(request).read()
    html = bs(response, 'html.parser')
    products_information = extract_products_information(html)
    result.extend(products_information)
  except Exception as e:
    logging.error('Failure processing: {}'.format(url))
    logging.error(e)
  return result