import logging
import configparser
from pathlib import Path
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from .utils import save_into_csv
from .extractors import extract_products_information
from ..utils import set_query_string_parameter_from_url

config = configparser.RawConfigParser()
config.read('{}/scraper.properties'.format(Path().absolute()))
TOTTUS = dict(config.items('TOTTUS'))

PAGINATION_INCREMENT = int(TOTTUS['pagination_increment'])
MAX_TRIES = int(TOTTUS['max_tries'])

def scrap(entries):
  print('Starting Tottus')
  logging.info('Processing Tottus')
  information = process_entries(entries)
  save_into_csv(information)
  print('Tottus done...')
  logging.info('Ending Tottus')

def should_continue(html):
  result = html.findAll('div', {'style' : 'width: 100%;height: 200px;float: left;'})
  if len(result) == 0:
    return True
  return False

def process_entries(entries):
  result = list()
  for entry in entries:
    information = process_entry(entry)
    result.extend(information)
  return result

def process_entry(entry):
  index = 0
  tries = 0
  result = list()
  while True:
    url = set_query_string_parameter_from_url(entry, 'No', index)
    print('Processing: {}'.format(url))
    request = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    try:
      response = urlopen(request).read()
      html = bs(response, 'html.parser')
      if not should_continue(html):
        break
      products_information = extract_products_information(html)
      result.extend(products_information)
      tries = 0
    except Exception as e:
      tries += 1
      logging.error('Failure processing: {}'.format(url))
      logging.error(e)
      if tries == MAX_TRIES:
        logging.error('Skipping rest of calls: {}'.format(url))
        return result
    index += PAGINATION_INCREMENT
  return result