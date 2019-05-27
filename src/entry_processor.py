from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from extractors import extract_products_information

pagination_increment = 10

def should_continue(soup):
  result = soup.findAll('div', {"style" : "width: 100%;height: 200px;float: left;"})
  if len(result) == 0:
    return True
  return False

def process_entry(entry):
  index = 0
  result = list()
  while True:
    url = str(entry).format(index)
    print('Calling: {}'.format(url))
    request = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    try:
      response = urlopen(request).read()
      html = bs(response, 'html.parser')
      if not should_continue(html):
        break
      products_information = extract_products_information(html) # VER extract_products_information(html)
      result.extend(products_information)
    except:
      print('Failure calling: {}'.format(url))
    index += pagination_increment
  return result