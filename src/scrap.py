from utils import load_urls, save_into_csv
from entry_processor import process_entries

entries = load_urls()
information = process_entries(entries)
save_into_csv(information)
print('Done...')