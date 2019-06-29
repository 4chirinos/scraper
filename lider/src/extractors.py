def extract_total_products(data):
  return data['results'][0]['nbHits']

def extract_products(data):
  return data['results']