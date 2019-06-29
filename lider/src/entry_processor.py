import json
from urllib.request import Request, urlopen
from extractors import extract_total_products, extract_products

URL = 'https://529cv9h7mw-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.32.1%3Breact-instantsearch%205.4.0%3BJS%20Helper%202.26.1&x-algolia-application-id=529CV9H7MW&x-algolia-api-key=c6ab9bc3e19c260e6bad42abe143d5f4'

def prepare_request(entry, n_products_to_retrieve):
  request = entry['requests'][0]
  params = request['params']
  request['params'] = params.format(n_products_to_retrieve)

def get_data(entry, n_products_to_retrieve):
  prepare_request(entry, n_products_to_retrieve)
  data = json.dumps(entry).encode('utf8')
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

  total_products = extract_total_products(get_data(entry, 1))
  products = extract_products(get_data(entry, total_products))

  #print(response)
    
  return result