from .models import ProductInformation

def extract_products(data):
  return data['hits']

def extract_product_information(product):
  if is_product_active(product):
    name = product['name']
    sku = product['sku']
    measure = product['uom']
    price = get_price(product)
    return ProductInformation(name, sku, price, measure)
  return None

def get_price(product):
  first_store = list(product['stores'].keys())[0]
  store = product['stores'][first_store]
  return store['prices']['sale']

def is_product_active(product):
  for store_id in list(product['stores'].keys()):
    store = product['stores'][store_id]
    if store['enabled']:
      return True
  return False