import requests

def get_ticket_info(event_id: int):
    url = f"https://www.bilesuparadize.lv/api/event/{event_id}/metadata"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    price_groups = data["price_groups"]

    # TODO: jaiegust informaciju ar linku par auditorijas vizualizaciju
    venue_labels = data["labels_json_url"]

    aggregated = {}
    for group in price_groups:
        price = group["price"]
        count = group["count"]
        if price not in aggregated:
            aggregated[price] = {"price": price, "available_seats": 0}
        aggregated[price]["available_seats"] += count


    results = sorted(aggregated.values(), key=lambda x: x["price"])

    ##print(results)

    return results

def get_event_info(event_id: int):
    url = f"https://www.bilesuparadize.lv/api/event/{event_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # TODO: jaiegust infromacija par bilesu tirgosanas laiku(sales_start, sales_end), aprakstu (main_description:lv), ilgumu (general_information:lv:duration), valodu (general_information:lv:language), norises vietas id (venue_id),
    event_name = data["performance"]["title"]
    event_date = data["date_time"]

    result = [event_id,event_name,event_date]

    ##print(result)
    return result


# TODO: izveidot funkciju, kas iegust info par norises vietam (nosaukums, adrese, etc)


def main():
    get_event_info(159795)
    get_ticket_info(159795)


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
