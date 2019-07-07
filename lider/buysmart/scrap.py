import json, copy
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from .utils import save_into_csv
from .extractors import extract_total_products, extract_products, extract_product_information

URL = 'https://529cv9h7mw-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.32.1%3Breact-instantsearch%205.4.0%3BJS%20Helper%202.26.1&x-algolia-application-id=529CV9H7MW&x-algolia-api-key=c6ab9bc3e19c260e6bad42abe143d5f4'

def scrap(entries):
  information = process_entries(entries)
  save_into_csv(information)
  print('Líder buysmart done...')

def prepare_payload(entry, n_products_to_retrieve):
  entry_copy = copy.deepcopy(entry)
  payload = entry_copy['requests'][0]
  params = payload['params']
  payload['params'] = params.format(n_products_to_retrieve)
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
  print('Processing entry: {}'.format(entry))
  try:
    total_products = extract_total_products(get_data(entry, 1))
    products = extract_products(get_data(entry, total_products))
    for product in products:
      product_information = extract_product_information(product)
      result.append(product_information)
  except:
    print('Failure processing entry: {}'.format(entry))
  return result