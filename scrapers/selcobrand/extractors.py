from .models import ProductInformation

def get_products(html):
  return html.find_all('div', class_ = 'product clickable')

def get_product_name(product):
  name = product.find('span', class_ = 'product-name truncate')
  description = product.find('span', class_ = 'product-info truncate')
  return '{} - {}'.format(name.text.strip(), description.text.strip())

def get_regular_price(product):
  price = product.find('span', class_ = 'price selling')
  if not price:
    return 0
  return price.text.strip()

def get_current_price(product):
  price = product.find('span', class_ = 'price')
  return price.text.strip()

def get_measure(product):
  measure = product.find('span', class_ = 'option-value-catalog')
  return measure.text.strip()

def extract_product_information(product):
  name = get_product_name(product)
  regular_price = get_regular_price(product)
  current_price = get_current_price(product)
  measure = get_measure(product)
  product_information = ProductInformation(name, regular_price, current_price, measure)
  return product_information

def extract_products_information(html):
  information = list()
  products = get_products(html)
  for product in products:
    product_information = extract_product_information(product)
    information.append(product_information)
  return information