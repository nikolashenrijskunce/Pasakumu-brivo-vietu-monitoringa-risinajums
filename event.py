import psycopg2
import requests

# TODO: jasanem int list un tad javeic iteracijas ar to
# update veic biezi
def get_ticket_info(event_id):
    # define galveni, ko raksta api izsaukuma, lai apietu bot filter
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.bilesuparadize.lv/",
    }

    # veic savienojumu ar datubazi
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        user='postgres',
        password='jojosiwa',
    )
    cur = conn.cursor()

    for i in event_id:
        # veic api izsaukumu bilesu paradizei, kas iegust JSON par bilesu kategorijam, cenam un skaitu
        url = f"https://www.bilesuparadize.lv/api/event/{i}/metadata"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # nem no json faila informaciju par visam cenu kategorijam un pa vienai pivieno datubaze
        price_groups = data["price_groups"]
        for group in price_groups:
            price = group["price"]
            count = group["count"]
            category = group["type"]

            # ievieto informacijju datu baze
            cur.execute("""
                INSERT INTO tickets (event_id, category, price, count)
                VALUES (%s, %s, %s, %s)

                ON CONFLICT (event_id, price)
        
                DO UPDATE SET
                category = EXCLUDED.category,
                count = EXCLUDED.count,
                checked_on = NOW()

                WHERE
                tickets.count IS DISTINCT FROM EXCLUDED.count
                OR
                tickets.category IS DISTINCT FROM EXCLUDED.category;""",
            (event_id, category, price, count))

            conn.commit()
    cur.close()
    conn.close()

    # results = sorted(aggregated.values(), key=lambda x: x["price"])
    # print(results)
    #
    # return results


# update 1 reizi diena
def get_event_info(event_id):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.bilesuparadize.lv/",
    }

    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        user='postgres',
        password='jojosiwa',
    )
    cur = conn.cursor()

    for i in event_id:
        url = f"https://www.bilesuparadize.lv/api/event/{i}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # dati par notikumu
        event_title = data["performance"]["title"]
        event_date = data["date_time"]
        event_sales_start = data["sales_start"]
        event_sales_end = data["sales_end"]
        event_description = data["performance"]["main_description"]["lv"]
        event_language = data["performance"]["general_information"]["lv"]["language"]
        event_venue = int(data["hall"]["venue_id"])

        # dati par koncertzali
        venue_id = event_venue
        venue_name = data["hall"]["title"]
        venue_address = data["hall"]["address"]
        venue_longitude = data["hall"]["venue"]["longitude"]
        venue_latitude = data["hall"]["venue"]["latitude"]

        # ievieto datus par koncertzalem datubaze
        cur.execute("""
            INSERT INTO venues (id, name, address, longitude, latitude)
            VALUES (%s, %s, %s, %s, %s)
            
            ON CONFLICT (id)
            
            DO UPDATE SET
            name = EXCLUDED.name,
            address = EXCLUDED.address,
            longitude = EXCLUDED.longitude,
            latitude = EXCLUDED.latitude
            
            WHERE
            venues.name IS DISTINCT FROM EXCLUDED.name
            OR
            venues.address IS DISTINCT FROM EXCLUDED.address
            OR
            venues.longitude IS DISTINCT FROM EXCLUDED.longitude
            OR
            venues.latitude IS DISTINCT FROM EXCLUDED.latitude;""",
        (venue_id, venue_name, venue_address, venue_longitude, venue_latitude))
        conn.commit()

        # ievieto datus par notikumiem datubaze
        cur.execute("""
            INSERT INTO events (id, title, date, sales_start, sales_end, description, language, venue_id)
            VALUES (%s, %s, %s, %s, %s %s, %s, %s) 
                
            ON CONFLICT (id)
        
            DO UPDATE SET
            title = EXCLUDED.title,
            date = EXCLUDED.date,
            sales_start = EXCLUDED.sales_start,
            sales_end = EXCLUDED.sales_end
            description = EXCLUDED.description,
            language = EXCLUDED.language,
            venue_id = EXCLUDED.venue_id
        
            WHERE
            events.title IS DISTINCT FROM EXCLUDED.title
            OR
            events.date IS DISTINCT FROM EXCLUDED.date
            OR
            events.sales_start IS DISTINCT FROM EXCLUDED.sales_start
            OR
            events.sales_end IS DISTINCT FROM EXCLUDED.sales_end
            OR
            events.description IS DISTINCT FROM EXCLUDED.description
            OR
            events.language IS DISTINCT FROM EXCLUDED.language
            OR
            events.venue_id IS DISTINCT FROM EXCLUDED.venue_id;""",
        (event_id, event_title, event_date, event_sales_start, event_sales_end, event_description, event_language, event_venue))
        conn.commit()
    cur.close()
    conn.close()

    # result = [event_id,event_title,event_date, event_sales_start, event_sales_end, event_description]
    # print(result)
    # return result



# testesanai
def main():
    event_id = 155961

    # get_event_info(event_id)
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
