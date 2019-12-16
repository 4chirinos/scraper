from .models import ProductInformation

def extract_total_products(data):
  return data['results'][0]['nbHits']

def extract_products(data):
  return data['results'][0]['hits']

def extract_product_information(product):
  name = product['displayName']
  regular_price = product['price']['BasePriceReference']
  current_price = product['price']['BasePriceSales']
  sku = product['sku']
  id = product['id']
  product_information = ProductInformation(name, regular_price, current_price, sku, id)
  return product_information