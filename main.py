import logging
import tottus, lider
from utils.common import load_entries
from pathlib import Path

def main():
  logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='scraper.log', level=logging.INFO)
  logging.info('Started')
  start()
  logging.info('Finished')

def start():
  path = Path().absolute()
  tottus_entries = load_entries('{}/entries/tottus_entries.json'.format(path))
  lider_buysmart_entries = load_entries('{}/entries/lider_smartbuy_entries.json'.format(path))
  lider_supermarket_entries = load_entries('{}/entries/lider_supermarket_entries.json'.format(path))
  tottus.scrap(tottus_entries)
  lider.buysmart.scrap(lider_buysmart_entries)
  lider.supermarket.scrap(lider_supermarket_entries)

if __name__ == '__main__':
  main()