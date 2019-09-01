import logging
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from .utils import save_into_csv
from .extractors import extract_products_information

page_increment = 1
max_tries = 10

def scrap(entries):
  logging.info('Processing Selcobrand')
  information = process_entries(entries)
  save_into_csv(information)
  print('Selcobrand done...')
  logging.info('Ending Selcobrand')

def should_continue(html):
  result = html.findAll('div', {'data-hook' : 'products_search_results_heading_no_results_found'})
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
  page = 1
  tries = 0
  result = list()
  while True:
    url = '{}?current_store_id=1&page={}'.format(entry, page)
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
    except:
      tries += 1
      logging.error('Failure processing: {}'.format(url))
      if tries == max_tries:
        logging.error('Skipping rest of calls: {}'.format(url))
        return result
    page += page_increment
  return result