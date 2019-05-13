from models import ProductInformation

def encode_utf8(to_encode):
  return to_encode.encode('utf-8')

def get_products(html):
  return html.find_all('div', class_ = 'item-product-caption')

def get_regular_price(price):
  if price is None:
    return 0
  return encode_utf8(str(price.text)).strip()

def get_current_price(price):
  return encode_utf8(str((price).span.text)).strip()

def get_product_name(product):
  title = product.find('div', class_ = 'title')
  name = encode_utf8(str(title.a.h5.div.text)).strip()
  return name

def extract_product_information(product):
  name = get_product_name(product)
  regular_price = get_regular_price(product.find('span', class_ = 'nule-price'))
  current_price = get_current_price(product.find('span', class_ = 'active-price'))
  product_information = ProductInformation(name, regular_price, current_price)
  return product_information

def extract_products_information(html):
  information = list()
  products = get_products(html)
  for product in products:
    product_information = extract_product_information(product)
    information.append(product_information)
  return information