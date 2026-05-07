import requests

def get_ticket_info(event_id: int):
    url = f"https://www.bilesuparadize.lv/api/event/{event_id}/metadata"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    price_groups = data["price_groups"]

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

    event_name = data["performance"]["title"]
    event_date = data["date_time"]

    result = [event_id,event_name,event_date]

    ##print(result)
    return result

def main():
    get_event_info(159795)
    get_ticket_info(159795)


if __name__ == "__main__":
    main()