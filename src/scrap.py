from utils import load_urls, process_entries, save_into_csv

entries = load_urls()
information = process_entries(entries)
save_into_csv(information)
print('Done...')