from models import ProductInformation

def get_products(html):
  return html.find_all('div', class_ = 'product-item-box')

def get_product_name(product):
  name = product.find('span', class_ = 'product-name')
  description = product.find('span', class_ = 'product-description')
  return '{} {}'.format(name.text.strip(), description.text.strip())

def get_measure(product):
  measure = product.find('span', class_ = 'product-attribute')
  return measure.text.strip()

def get_current_price(product):
  current_price = product.find('span', class_ = 'price-sell')
  return current_price.text.strip()

def get_regular_price(product):
  regular_price = product.find('span', class_ = 'price-internet')
  if not regular_price:
    return 0
  return regular_price.text.replace('Normal:', '').strip()

def get_price_measure_relation(product):
  price_measure_relation = product.find('span', class_ = 'product-round')
  return price_measure_relation.text.strip()

def extract_product_information(product):
  name = get_product_name(product)
  regular_price = get_regular_price(product)
  current_price = get_current_price(product)
  measure = get_measure(product)
  price_measure_relation = get_price_measure_relation(product)
  product_information = ProductInformation(name, regular_price, current_price, measure, price_measure_relation)
  return product_information

def extract_products_information(html):
  information = list()
  products = get_products(html)
  for product in products:
    product_information = extract_product_information(product)
    information.append(product_information)
  return information