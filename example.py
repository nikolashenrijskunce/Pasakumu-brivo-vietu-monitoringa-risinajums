import psycopg2

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


# id = search.get_all_event_ids()
# event.get_event_info(id)
# event.get_ticket_info(id)
#
# conn = psycopg2.connect(
#         host='localhost',
#         port='5432',
#         user='postgres',
#         password='jojosiwa',
#     )
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM events;")
#
# # Fetch all rows
# rows = cur.fetchall()
#
# # Print rows
# for row in rows:
#     print(row)