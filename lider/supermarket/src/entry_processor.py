from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from extractors import extract_products_information

MAX_PRODUCTS = 5000

def process_entries(entries):
  result = list()
  for entry in entries:
    information = process_entry(entry)
    result.extend(information)
  return result

def process_entry(entry):
  result = list()
  url = entry.format(MAX_PRODUCTS)
  print('Calling: {}'.format(url))
  request = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
  try:
    response = urlopen(request).read()
    html = bs(response, 'html.parser')
    products_information = extract_products_information(html)
    result.extend(products_information)
  except:
    print('Failure calling: {}'.format(url))
  return result