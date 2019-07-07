import tottus, lider
from utils.common import load_entries
from pathlib import Path

path = Path().absolute()

tottus_entries = load_entries('{}/tottus_entries.json'.format(path))
lider_buysmart_entries = load_entries('{}/lider_smartbuy_entries.json'.format(path))
lider_supermarket_entries = load_entries('{}/lider_supermarket_entries.json'.format(path))

tottus.scrap(tottus_entries)
lider.buysmart.scrap(lider_buysmart_entries)
lider.supermarket.scrap(lider_supermarket_entries)