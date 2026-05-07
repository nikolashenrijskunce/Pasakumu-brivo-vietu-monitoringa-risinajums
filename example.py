import event
import search

id = search.get_all_event_ids()
event_name = []
event_price =[]

for i in range(900,910):
    event_name.append(event.get_event_info(id[i]))
    event_price.append(event.get_ticket_info(id[i]))

for i in range(10):
    print(event_name[i]+event_price[i])