from .models import ProductInformation

def get_products(html):
  return html.find_all('div', class_ = 'item-product-caption')

def get_regular_price(product):
  price = product.find('span', class_ = 'nule-price')
  if not price:
    return 0
  return price.text.strip()

def get_current_price(product):
  price = product.find('span', class_ = 'active-price')
  return price.span.text.strip()

def get_product_name(product):
  title = product.find('div', class_ = 'title')
  return title.a.h5.div.text.strip()

def get_measure(product):
  statement = product.find('div', class_ = 'statement')
  return statement.text.strip()

def get_promotions(product):
  offer_details = product.find('div', class_ = 'offer-details')
  promotions = offer_details.find('span', class_ = 'red')
  if not promotions:
    return 'N/A'
  return promotions.text.strip()

def get_promotions_period(product):
  offer_details = product.find('div', class_ = 'offer-details')
  promotions = offer_details.find('span', class_ = 'conditions')
  if not promotions:
    return 'N/A'
  period = promotions.get('title')
  return period.strip()

def extract_product_information(product):
  name = get_product_name(product)
  regular_price = get_regular_price(product)
  current_price = get_current_price(product)
  measure = get_measure(product)
  promotions = get_promotions(product)
  promotions_period = get_promotions_period(product)
  product_information = ProductInformation(name, regular_price, current_price, measure, promotions, promotions_period)
  return product_information

def extract_products_information(html):
  information = list()
  products = get_products(html)
  for product in products:
    product_information = extract_product_information(product)
    information.append(product_information)
  return information