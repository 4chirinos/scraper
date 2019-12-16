import logging
import scrapers
from utils.common import load_entries
from pathlib import Path

def main():
  logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', filename = 'scraper.log', level = logging.INFO)
  logging.info('Started')
  start()
  logging.info('Finished')

def start():
  path = Path().absolute()
  #tottus_entries = load_entries('{}/entries/tottus_entries.json'.format(path))
  lider_buysmart_entries = load_entries('{}/entries/lider_smartbuy_entries.json'.format(path))
  lider_supermarket_entries = load_entries('{}/entries/lider_supermarket_entries.json'.format(path))
  selcobrand_entries = load_entries('{}/entries/selcobrand_entries.json'.format(path))
  #scrapers.tottus.scrap(tottus_entries)
  scrapers.lider.buysmart.scrap(lider_buysmart_entries)
  #scrapers.lider.supermarket.scrap(lider_supermarket_entries)
  #scrapers.selcobrand.scrap(selcobrand_entries)

if __name__ == '__main__':
  main()