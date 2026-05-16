import event
import search
import time

id = []
next_scrape_time = 0.0

while True:
    if time.time() > next_scrape_time:
        print("Scraping")
        id = search.get_all_event_ids()
        next_scrape_time = time.time() + 86400.0
        event.get_event_info(id)
    print("getting api")
    event.get_ticket_info(id)
    time.sleep(900)