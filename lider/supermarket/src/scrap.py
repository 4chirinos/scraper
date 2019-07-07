from utils import load_entries, save_into_csv
from entry_processor import process_entries

entries = load_entries()
information = process_entries(entries)
save_into_csv(information)
print('Líder supermarket done...')