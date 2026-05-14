import requests

def get_ticket_info(event_id: int):

    # veic api izsaukumu bilesu paradizei, kas iegust JSON par bilesu kategorijam, cenam un skaitu
    url = f"https://www.bilesuparadize.lv/api/event/{event_id}/metadata"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # TODO: JAPARBAUDA jaiegust informaciju ar linku par auditorijas vizualizaciju
    venue_labels = data["labels_json_url"]

    # izvellk bilesu informaciju no JSON faila
    price_groups = data["price_groups"]
    aggregated = {}

    for group in price_groups:
        price = group["price"]
        count = group["count"]
        if price not in aggregated:
            aggregated[price] = {"price": price, "available_seats": 0}
        aggregated[price]["available_seats"] += count

    results = sorted(aggregated.values(), key=lambda x: x["price"])

    return results



def get_event_info(event_id: int):
    url = f"https://www.bilesuparadize.lv/api/event/{event_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # TODO: JAPARBAUDA dati par notikumu
    event_name = data["performance"]["title"]
    event_date = data["date_time"]
    event_sales_start = data["sales_start"]
    event_sales_end = data["sales_end"]
    event_description = data["main_description"]
    event_duration = data["general_information"]
    event_language = data["general_information"]
    event_venue = data["hall"]["venue_id"]
    # event_description = event_description

    #TODO: JAPARBAUDA dati par koncertzali
    venue_id = event_venue
    venue_name = data["hall"]["title"]
    venue_address = data["hall"]["address"]
    venue_longitude = data["hall"]["venue"]["longitude"]
    venue_latitude = data["hall"]["venue"]["latitude"]


    # result = [event_id,event_name,event_date, event_sales_start, event_sales_end, event_description]
    result = type(event_description)
    print(result)
    return result



def main():
    event_id = 0

    get_event_info(event_id)
    get_ticket_info(event_id)



if __name__ == "__main__":
    main()



# iegust informaciju par visiem events un to norises laikiem no
# https://www.bilesuparadize.lv/api/venue/1589/event
# IEGUST: visas izrades, kas norisinas

# iegust visadu informaciju par pasakumu
# https://www.bilesuparadize.lv/api/event/164863
# IEGUST: notikuma datums, bilesu pardosanas periods, nosaukums, atteli, apraksts, ilgums, valoda, norises vieta, koordinates, adrese

# iegust info par brivajam vietam un cenam
# https://www.bilesuparadize.lv/api/event/159795/metadata
# IEGUST: links uz json dokumentu ar sedvietu vizualizacijas rakstiem, sedvietu cenas, brivo sedvietu skaits

# iegust vizualo auditorijas vietu izkartojumu
# https://www1.bilesuparadize.lv/layouts/event-164863-.txt
# IEGUST: sedvietu izvietojuma vizualizacija svg fromata

# uzraksti prieks visuala izkartojuma
# https://www2.bilesuparadize.lv/layouts/event-164863-labels.json
# IEGUST: apraksti vizualizacijai
