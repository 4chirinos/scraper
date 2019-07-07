import logging
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from .utils import save_into_csv
from .extractors import extract_products_information

pagination_increment = 10
max_tries = 10

def scrap(entries):
  information = process_entries(entries)
  save_into_csv(information)
  print('Tottus done...')

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
    url = entry.format(index)
    print('Calling: {}'.format(url))
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
      logging.error('Failure calling: {}'.format(url))
      if tries == max_tries:
        logging.error('Skipping rest of calls: {}'.format(url))
        return result
    index += pagination_increment
  return result