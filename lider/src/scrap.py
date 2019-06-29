from utils import load_entries
from entry_processor import process_entries

url = 'https://529cv9h7mw-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.32.1%3Breact-instantsearch%205.4.0%3BJS%20Helper%202.26.1&x-algolia-application-id=529CV9H7MW&x-algolia-api-key=c6ab9bc3e19c260e6bad42abe143d5f4'

entries = load_entries()

process_entries(entries)